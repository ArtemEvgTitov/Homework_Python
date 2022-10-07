# import operations as oper
import logger as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from settings import TOKEN