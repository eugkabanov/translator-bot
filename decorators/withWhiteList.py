from telegram import Update
from telegram.ext import ContextTypes

from config import ALLOWED_USERS
import logging

logger = logging.getLogger(__name__)

# This is a list of allowed users. You can add user IDs or usernames in config.
allowed_users = ALLOWED_USERS


def withWhiteList(handler):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        username = update.effective_user.username

        if user_id not in allowed_users and username not in allowed_users:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Sorry, you don't have access to this bot.",
            )
            logger.warning(
                f"Unauthorized access attempt by user: {user_id} / {username}"
            )

            # Returning None will stop the handler chain.
            return

        return await handler(update, context)

    return wrapper
