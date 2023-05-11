from main import user_language_prefs
from telegram import Update
from telegram.ext import ContextTypes

from utils import translate


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    # Extract the text from the user's message
    user_text = update.message.text

    # Extract the user's language preference. Default to Spanish if not set.
    target_language = user_language_prefs.get(chat_id, "Spanish")

    # Translate the text
    translated_text = translate(user_text, target_language)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=translated_text
    )
