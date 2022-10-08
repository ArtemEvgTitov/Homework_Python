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

tel_numb = {"id": 0, "surname": '', "name": '', "tel": '', "coment": ''}
contact = []


def save():
    with open("tel_numb.json", "w", encoding="utf-8") as tel:
        tel.write(json.dumps(tel_numb, ensure_ascii=False))


def load():
    global contact
    try:
        with open("contacts.json", "r", encoding="utf-8") as cont:
            contact = json.load(cont)
    except:
        contact = []


def add_contact(tel_numb):
    try:
        load()
        temp = []
        ID = False
        for i in contact:
            temp.append(i["id"])
        while ID == False:
            if tel_numb["id"] in temp:
                tel_numb["id"] += 1
            else:
                ID = True
        contact.append(tel_numb)
        with open("contacts.json", "w", encoding="utf-8") as cont:
            cont.write(json.dumps(contact, ensure_ascii=False))
        log.text_in_log(
            f"В телефонную книгу добавлен контакт: \n+++ {tel_numb['surname']} {tel_numb['name']} тел. {tel_numb['tel']}")
    except:
        contact.append(tel_numb)
        with open("contacts.json", "w", encoding="utf-8") as cont:
            cont.write(json.dumps(contact, ensure_ascii=False))
        log.text_in_log(
            f"В телефонную книгу добавлен контакт: \n+++ {tel_numb['surname']} {tel_numb['name']} тел. {tel_numb['tel']}")


SURNAME, NAME, TEL, COMMENT = range(4)

ALL_CONTACTS, EDITING, DELETE = range(3)


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


def surname(update, _):
    if (update.message.text).isalpha() == False:
        log.text_in_log("Некорректный ввод фамилии - {update.message.text}")
        update.message.reply_text(
            'Фамилия введена некорректно. Повторите ввод')
        return SURNAME
    tel_numb['surname'] = update.message.text
    save()
    log.text_in_log(f"Введена фамилия - {update.message.text}")
    update.message.reply_text('Введите имя')
    return NAME


def name(update, _):
    if (update.message.text).isalpha() == False:
        log.text_in_log("Некорректный ввод имени - {update.message.text}")
        update.message.reply_text('Имя введено некорректно. Повторите ввод')
        return NAME
    tel_numb['name'] = update.message.text
    save()
    log.text_in_log(f"Введено имя - {update.message.text}")
    update.message.reply_text('Введите номер телефона без +')
    return TEL


def tel(update, _):
    if (update.message.text).isdigit() == False:
        log.text_in_log(
            f"Некорректный ввод номера телефона - {update.message.text}")
        update.message.reply_text('Номер введён неверно. Повторите ввод')
        return TEL
    load()
    for i in contact:
        if i["tel"] == update.message.text:
            log.text_in_log(
                f"Ввод повторяющегося номера телефона - {update.message.text}")
            update.message.reply_text(
                f'Такой номер телефона уже принадлежит контакту - {i["surname"]} {i["name"]}. \nПовторите ввод либо введите команду \n/cancel')
            return TEL
    tel_numb['tel'] = update.message.text
    save()
    log.text_in_log(f"Введён номер телефона - {update.message.text}")
    update.message.reply_text('Введите коментарий к контакту')
    return COMMENT


def comment(update, _):
    tel_numb['coment'] = update.message.text
    save()
    log.text_in_log(f"Введён коментарий - {update.message.text}")
    add_contact(tel_numb)
    return ConversationHandler.END


def all_contacts(update, _):
    pass


def editing(update, _):
    pass


def delete(update, _):
    pass


def message(update, _):
    text = update.message.text
    if text == 'Создать контакт':
        log.text_in_log('Нажата кнопка "Создать контакт"')
        update.message.reply_text(
            'Для отмены введите /cancel\n\nВведите фамилию')
        return SURNAME


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    record_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, message)],
        states={
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, surname)],
            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            TEL: [MessageHandler(Filters.text & ~Filters.command, tel)],
            COMMENT: [MessageHandler(Filters.text & ~Filters.command, comment)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    base_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, message)],
        states={
            ALL_CONTACTS: [MessageHandler(Filters.text & ~Filters.command, all_contacts)],
            EDITING: [MessageHandler(Filters.text & ~Filters.command, editing)],
            DELETE: [MessageHandler(Filters.text & ~Filters.command, delete)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(record_handler)
dispatcher.add_handler(base_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
