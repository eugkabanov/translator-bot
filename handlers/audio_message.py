import os
import logging
from main import user_language_prefs
from telegram import Update, Voice, Audio
from telegram.ext import ContextTypes
from utils import convert_audio, create_transcription, translate

AUDIO_FILES_PATH = "audio_files"


async def audio_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger = logging.getLogger(__name__)
    chat_id = update.effective_chat.id

    message = update.message

    if isinstance(message.voice, Voice):
        file_id = message.voice.file_id
        original_extension = ".ogg"
    elif isinstance(message.audio, Audio):
        file_id = message.audio.file_id

        file_name, file_extension = os.path.splitext(message.audio.file_name)
        original_extension = file_extension
    else:
        return

    # final text to send to user
    text = "Something went wrong. Please try again."

    try:
        # Use the getFile method to get a file_path
        file = await context.bot.get_file(file_id)

        # Download the file
        # Whisper requires the file to be in mp3 format
        ORIGINAL_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}{original_extension}"
        CONVERTED_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}.mp3"

        # Create the audio_files directory if it doesn't exist
        if not os.path.exists(AUDIO_FILES_PATH):
            os.makedirs(AUDIO_FILES_PATH)

        # Download the file
        await file.download_to_drive(ORIGINAL_AUDIO_PATH)

        # Convert the ogg file to mp3, as Whisper requires wav format
        converted_path = convert_audio(ORIGINAL_AUDIO_PATH, CONVERTED_AUDIO_PATH)

        if converted_path is None:
            # Stop the function from continuing
            raise RuntimeError(
                "There was an error converting your audio file. Please try again."
            )

        # Create a transcription
        transcript = create_transcription(CONVERTED_AUDIO_PATH)

        if transcript is None:
            # Stop the function from continuing
            raise RuntimeError(
                "There was an error transcribing your audio file. Please try again.",
            )

        # Extract the user's language preference. Default to Spanish if not set.
        target_language = user_language_prefs.get(chat_id, "Spanish")

        # Translate the text
        text = translate(transcript, target_language)

    except RuntimeError as e:
        text = str(e)

    except OSError as e:
        logger.error(e.strerror)

    finally:
        try:
            # Delete the audio files
            os.remove(ORIGINAL_AUDIO_PATH)
            os.remove(CONVERTED_AUDIO_PATH)
        except OSError as e:
            logger.error(e.strerror)

        # Send output to user
        await context.bot.send_message(
            chat_id, f"From audio: {transcript} \n\nTranslated: \n\n{text}"
        )
