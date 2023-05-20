import os
import logging
from main import user_language_prefs
from telegram import Update, Voice
from telegram.ext import ContextTypes
from utils import convert_audio, create_transcription, translate

AUDIO_FILES_PATH = "audio_files"


async def voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    voice: Voice = update.message.voice
    file_id = voice.file_id

    # Use the getFile method to get a file_path
    file = context.bot.get_file(file_id)

    # Download the file
    # Whisper requires the file to be in wav format
    ORIGINAL_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}.ogg"
    CONVERTED_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}.wav"

    if not os.path.exists(AUDIO_FILES_PATH):
        os.makedirs(AUDIO_FILES_PATH)
    file.download(ORIGINAL_AUDIO_PATH)

    # Convert the ogg file to wav, as Whisper requires wav format
    try:
        convert_audio(ORIGINAL_AUDIO_PATH, CONVERTED_AUDIO_PATH)
    except Exception as e:
        logger = logging.getLogger(__name__)

        logger.error(e)
        context.bot.send_message(
            chat_id,
            text="There was an error converting your audio file. Please try again.",
        )
        return

    transcript = await create_transcription(CONVERTED_AUDIO_PATH)

    # Extract the user's language preference. Default to Spanish if not set.
    target_language = user_language_prefs.get(chat_id, "Spanish")

    # Translate the text
    translated_text = translate(transcript, target_language)

    context.bot.send_message(chat_id, text=translated_text)
