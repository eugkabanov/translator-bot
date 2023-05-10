from telegram import Update
from telegram.ext import ContextTypes

from utils import translate


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the text from the user's message
    user_text = update.message.text

    # Tramslate the text
    translated_text = translate(user_text, "Spanish")

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=translated_text
    )
