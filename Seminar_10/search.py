import logger as log
from settings import TOKEN
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


def load():
    global contact
    try:
        with open("contacts.json", "r", encoding="utf-8") as cont:
            contact = json.load(cont)
    except:
        contact = []


SEARCH, END_SEARCH = range(2)


def start(update, _):
    log.text_in_log('---ЗАПУСК БОТА---')
    reply_keyboard = [['Создать контакт'], ['Поиск'], ['Все контакты']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        'Слушаю',
        reply_markup=markup_key,)


def cancel(update, _):
    log.text_in_log('Выход')
    update.message.reply_text(
        'Отмена записи',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def search(update, _):
    text = update.message.text
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    temp = []
    load()
    for i in contact:
        if text in i["surname"] or text in i["name"] or text in i["tel"]:
            temp.append(i)
    for i in temp:
        update.message.reply_text(
            f'№{i["id"]+1}. {i["surname"]} {i["name"]} тел. {i["tel"]} - {i["coment"]}\n',
            reply_markup=markup_key,)
    update.message.reply_text('Повторить поиск?')
    return END_SEARCH


def end_search(update, _):
    text = update.message.text
    if text == 'Нет':
        return ConversationHandler.END
    elif text == 'Да':
        update.message.reply_text('Введите данные для поиска')
        return SEARCH


def message(update, _):
    text = update.message.text
    if text == 'Поиск':
        log.text_in_log('Нажата кнопка "Поиск"')
        update.message.reply_text(
            'Введите данные для поиска')
        return SEARCH


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    search_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, message)],
        states={
            SEARCH: [MessageHandler(Filters.text & ~Filters.command, search)],
            END_SEARCH: [MessageHandler(Filters.text & ~Filters.command, end_search)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
