import os
from telegram import Update, Voice
from telegram.ext import ContextTypes
from utils import convert_audio

AUDIO_FILES_PATH = "audio_files"


async def voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice: Voice = update.message.voice
    file_id = voice.file_id

    # Use the getFile method to get a file_path
    file = context.bot.get_file(file_id)

    # Download the file
    ORIGINAL_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}.ogg"
    CONVERTED_AUDIO_PATH = f"{AUDIO_FILES_PATH}/{file_id}.wav"

    if not os.path.exists(AUDIO_FILES_PATH):
        os.makedirs(AUDIO_FILES_PATH)
    file.download(ORIGINAL_AUDIO_PATH)

    # Convert the ogg file to wav, as Whisper requires wav format
    convert_audio(ORIGINAL_AUDIO_PATH, CONVERTED_AUDIO_PATH)

    # TODO: Get transcription from Whisper API

    # TODO: Translate text and send back to the user
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="This is a placeholder message"
    )
