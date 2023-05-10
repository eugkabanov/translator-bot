import logging
from config import TELEGRAM_API_TOKEN
from telegram.ext import ApplicationBuilder
from handlers import start_handler, restrict_access_handler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Add handlers to application
    application.add_handler(start_handler)
    application.add_handler(restrict_access_handler)

    application.run_polling()
