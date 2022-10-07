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
    with open("contacts.json", "r", encoding="utf-8") as cont:
        contact = json.load(cont)


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
        log.text_in_log(f"В телефонную книгу добавлен контакт: \n+++ {tel_numb['surname']} {tel_numb['name']} тел. {tel_numb['tel']}")
    except:
        contact.append(tel_numb)
        with open("contacts.json", "w", encoding="utf-8") as cont:
            cont.write(json.dumps(contact, ensure_ascii=False))
        log.text_in_log(f"В телефонную книгу добавлен контакт: \n+++ {tel_numb['surname']} {tel_numb['name']} тел. {tel_numb['tel']}")


SURNAME, NAME, TEL, COMMENT = range(4)


def record(update, _):
    log.text_in_log("Запись контакта")
    update.message.reply_text('Для отмены введите /cancel\n\nВведите фамилию')
    return SURNAME


def cancel(update, _):
    log.text_in_log('Выход')
    update.message.reply_text(
        'Отмена записи',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def surname(update, _):
    tel_numb['surname'] = update.message.text
    save()
    log.text_in_log(f"Введена фамилия - {update.message.text}")
    update.message.reply_text('Введите имя')
    return NAME


def name(update, _):
    tel_numb['name'] = update.message.text
    save()
    log.text_in_log(f"Введено имя - {update.message.text}")
    update.message.reply_text('Введите номер телефона')
    return TEL


def tel(update, _):
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


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('record', record)],
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
