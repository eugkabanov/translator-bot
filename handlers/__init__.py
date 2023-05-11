from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters

from decorators import withWhiteList
from .start import start
from .message import message
from .language import language
from .language_select import language_select


start_handler = CommandHandler("start", withWhiteList(start))
language_handler = CommandHandler("language", withWhiteList(language))

language_select_handler = CallbackQueryHandler(withWhiteList(language_select))

message_handler = MessageHandler(filters.TEXT, withWhiteList(message))
