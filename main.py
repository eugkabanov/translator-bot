import logging
from config import TELEGRAM_API_TOKEN, OPENAI_API_KEY, ALLOWED_USERS
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

# List of allowed user IDs or usernames
allowed_users = ALLOWED_USERS

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Start message goes here"
    )


async def restricted_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    # Check if user ID or username is in list of allowed users
    if user_id not in allowed_users and username not in allowed_users:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, you don't have access to this bot.",
        )
        logger.warning(f"Unauthorized access attempt by user: {user_id} / {username}")
        return

    # Your chatbot functionality and message handling here
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="You passed security!"
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Define handlers here
    restricted_chat_handler = MessageHandler(
        filters.TEXT | filters.COMMAND, restricted_chat
    )
    start_handler = CommandHandler("start", start)

    # Add handlers to application
    application.add_handler(start_handler)
    application.add_handler(restricted_chat_handler)

    application.run_polling()
