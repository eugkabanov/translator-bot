from telegram.ext import CommandHandler, MessageHandler, filters

from .start import start
from .restrictAccess import restrict_access


start_handler = CommandHandler("start", start)
restrict_access_handler = MessageHandler(
    filters.TEXT | filters.COMMAND, restrict_access
)
