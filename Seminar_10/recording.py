import logger as log
from settings import TOKEN
import random
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


def save():
    global tel_numb
    with open("tel_numb.json", "w", encoding="utf-8") as reg:
        reg.write(json.dumps(tel_numb, ensure_ascii=False))


SURNAME, NAME, TEL, COMMENT = range(4)


def start():
    pass


def cancel():
    pass


def surname():
    pass


def name():
    pass


def tel():
    pass


def comment():
    pass


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, surname)],
            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            TEL: [MessageHandler(Filters.text & ~Filters.command, tel)],
            COMMENT: [MessageHandler(Filters.text & ~Filters.command, comment)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()