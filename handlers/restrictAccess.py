from config import ALLOWED_USERS
from telegram import Update
from telegram.ext import ContextTypes, filters
import logging

logger = logging.getLogger(__name__)

# This is a list of allowed users. You can add user IDs or usernames in config.
allowed_users = ALLOWED_USERS


async def restrict_access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if user_id not in allowed_users and username not in allowed_users:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, you don't have access to this bot.",
        )
        logger.warning(f"Unauthorized access attempt by user: {user_id} / {username}")
        return

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="You passed security!"
    )
