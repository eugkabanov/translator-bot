from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Hello there! 👋\n\n"
        "I'm your friendly Translator Bot. 🤖\n\n"
        "I'm here to help you with translations. I can detect the language of your input "
        "and translate it to a language of your choice. To get started, please choose your target language "
        "by typing /language command.\n\n"
        "Feel free to type any message, and I'll translate it for you! 🌐"
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_message,
    )
