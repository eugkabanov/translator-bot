from telegram.ext import CommandHandler, MessageHandler, filters

from decorators import withWhiteList
from .start import start


start_handler = CommandHandler("start", withWhiteList(start))
