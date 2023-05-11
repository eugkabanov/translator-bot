from main import user_language_prefs
from telegram import Update
from telegram.ext import ContextTypes


async def language_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    query = update.callback_query
    selected_language = query.data

    # Store user's language preference here
    user_language_prefs[chat_id] = selected_language

    await query.answer(f"Translator will translate into: {selected_language}")
