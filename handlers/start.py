from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 Hello and welcome! 🌍\n\n"
        "I'm your handy Translator Bot, powered by advanced AI that not only translates text but can also make it sound "
        "natural and idiomatic in your chosen language. 🤖🌐\n\n"
        "Moreover, I can translate voice messages from any messenger! Just forward them to this chat, and I'll do the rest. 🎙️➡️💬\n\n"
        "To get started, choose your preferred language by typing the /language command. Once that's set, you can send me any "
        "text or voice message, and I'll translate it for you. 🔄\n\n"
        "Whether it's for travel, learning a new language, or everyday communication, I'm here to make your life a bit easier. "
        "Let's break down those language barriers together! 👫🏽"
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_message,
    )
