from telegram import Update
from telegram.ext import ContextTypes


async def language_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    selected_language = query.data

    # Store user's language preference here
    # use a database or a data structure in memory

    await query.answer(f"You selected {selected_language}")
