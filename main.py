import logging
from config import TELEGRAM_API_TOKEN
from telegram.ext import ApplicationBuilder
import handlers

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Store user's language preference here
# key = chat_id, value = language
user_language_prefs: dict[int, str] = {}

if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Add handlers to application
    application.add_handler(handlers.start_handler)
    application.add_handler(handlers.language_handler)
    application.add_handler(handlers.language_select_handler)
    application.add_handler(handlers.message_handler)
    application.add_handler(handlers.voice_message_handler)
    application.add_handler(handlers.audio_message_handler)

    application.run_polling()
