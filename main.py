from config import TELEGRAM_API_TOKEN, OPENAI_API_KEY, ALLOWED_USERS
from telegram import Update
from telegram.ext import MessageHandler, Updater, filters

# List of allowed user IDs or usernames
allowed_users = ALLOWED_USERS


def restricted_chat(update: Update, context):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if user_id not in allowed_users and username not in allowed_users:
        update.message.reply_text("Sorry, you don't have access to this bot.")
        return

    # Your chatbot functionality and message handling here


updater = Updater(TELEGRAM_API_TOKEN)

dp = updater.dispatcher
dp.add_handler(MessageHandler(filters.Text & ~filters.Command, restricted_chat))

updater.start_polling()
updater.idle()
