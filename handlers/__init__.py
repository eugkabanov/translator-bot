from telegram.ext import CommandHandler, MessageHandler, filters

from decorators import withWhiteList
from .start import start
from .message import message


start_handler = CommandHandler("start", withWhiteList(start))
message_handler = MessageHandler(filters.TEXT, withWhiteList(message))
