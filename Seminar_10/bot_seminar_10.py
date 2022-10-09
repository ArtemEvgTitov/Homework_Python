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

SURNAME, NAME, TEL, COMMENT, SEARCH, END_SEARCH, DELETE_ALL, DEL_CONT, DEl_C = range(
    9)

tel_numb = {"id": 0, "surname": '', "name": '', "tel": '', "coment": ''}
contact = []


def save():
    with open("tel_numb.json", "w", encoding="utf-8") as tel:
        tel.write(json.dumps(tel_numb, ensure_ascii=False))
    log.text_in_log('Телефонная книга сохранена')


def load():
    global contact
    log.text_in_log('Телефонная книга загружена')
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


def start(update, _):
    reply_keyboard = [['Создать контакт', 'Поиск'], [
        'Все контакты', 'Удалить все контакты'], ['Удалить контакт']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        'Слушаю',
        reply_markup=markup_key,)


def cancel(update, _):
    log.text_in_log('Выход')
    update.message.reply_text(
        'Отмена',
        reply_markup=ReplyKeyboardRemove()
    )
    start(update, _)
    return ConversationHandler.END


def surname(update, _):
    if (update.message.text).isalpha() == False:
        log.text_in_log("Некорректный ввод фамилии - {update.message.text}")
        update.message.reply_text(
            'Фамилия введена некорректно. Повторите ввод\n/cancel')
        return SURNAME
    tel_numb['surname'] = update.message.text
    save()
    log.text_in_log(f"Введена фамилия - {update.message.text}")
    update.message.reply_text('Введите имя\n/cancel')
    return NAME


def name(update, _):
    if (update.message.text).isalpha() == False:
        log.text_in_log("Некорректный ввод имени - {update.message.text}")
        update.message.reply_text(
            'Имя введено некорректно. Повторите ввод\n/cancel')
        return NAME
    tel_numb['name'] = update.message.text
    save()
    log.text_in_log(f"Введено имя - {update.message.text}")
    update.message.reply_text('Введите номер телефона без +\n/cancel')
    return TEL


def tel(update, _):
    if (update.message.text).isdigit() == False:
        log.text_in_log(
            f"Некорректный ввод номера телефона - {update.message.text}")
        update.message.reply_text(
            'Номер введён неверно. Повторите ввод\n/cancel')
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
    update.message.reply_text('Введите коментарий к контакту\n/cancel')
    return COMMENT


def comment(update, _):
    tel_numb['coment'] = update.message.text
    save()
    log.text_in_log(f"Введён коментарий - {update.message.text}")
    add_contact(tel_numb)
    start(update, _)
    return ConversationHandler.END


def search(update, _):
    log.text_in_log('Запущен поиск')
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
    if temp == []:
        update.message.reply_text(
            'Я такого не нашёл :(', reply_markup=markup_key,)
        log.text_in_log('Поиск не дал результатов')
    update.message.reply_text('Повторить поиск?\n/cancel')
    return END_SEARCH


def end_search(update, _):
    text = update.message.text
    if text == 'Нет':
        log.text_in_log('Отмена повторного поиска')
        start(update, _)
        return ConversationHandler.END
    elif text == 'Да':
        log.text_in_log('Повторный поиск')
        update.message.reply_text('Введите данные для поиска\n/cancel')
        return SEARCH


def all_cont(update, _):
    load()
    temp = ''
    for i in contact:
        temp += f'№{i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["coment"]})\n---------------------\n'
    update.message.reply_text(temp)
    log.text_in_log('Вывод всех контактов на экран')
    start(update, _)


def delete_all(update, _):
    text = update.message.text
    if text == 'Да':
        path = 'contacts.json'
        f = open(path, 'w', encoding="utf-8")
        f.write('')
        f.close()
    update.message.reply_text('Все контакты удалены')
    start(update, _)
    if text == 'Нет':
        cancel(update, _)
    return ConversationHandler.END


def del_cont(update, _):
    load()
    text = int(update.message.text) - 1
    temp = {}
    for i in contact:
        if text == i['id']:
            temp = i
    with open("tel_numb.json", "w", encoding="utf-8") as tel:
        tel.write(json.dumps(temp, ensure_ascii=False))
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        f'Вы уверены, что хотите удалить {temp["surname"]} {temp["name"]}?\n/cancel', reply_markup=markup_key,)
    return DEl_C


def del_c(update, _):
    text = update.message.text
    if text == 'Да':
        load()
        with open("tel_numb.json", "r", encoding="utf-8") as tel_n:
            tel_num = json.load(tel_n)
        for i in contact:
            if i == tel_num:
                contact.remove(i)
        with open("contacts.json", "w", encoding="utf-8") as cont:
            cont.write(json.dumps(contact, ensure_ascii=False))
        update.message.reply_text('Готово')
        start(update, _)
    if text == 'Нет':
        cancel(update, _)
    return ConversationHandler.END


def message(update, _):
    text = update.message.text
    if text == 'Создать контакт':
        log.text_in_log('Нажата кнопка "Создать контакт"')
        update.message.reply_text(
            'Для отмены введите /cancel\n\nВведите фамилию')
        return SURNAME
    elif text == 'Поиск':
        log.text_in_log('Нажата кнопка "Поиск"')
        update.message.reply_text(
            'Введите данные для поиска\n/cancel')
        return SEARCH
    elif text == 'Все контакты':
        log.text_in_log('Нажата кнопка "Все контакты"')
        all_cont(update, _)
    elif text == 'Удалить все контакты':
        log.text_in_log('Нажата кнопка "Удалить все контакты"')
        reply_keyboard = [['Да', 'Нет']]
        markup_key = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(
            'Вы уверены, что хотите удалить все контакты?\n/cancel', reply_markup=markup_key,)
        return DELETE_ALL
    elif text == 'Удалить контакт':
        log.text_in_log('Нажата кнопка "Удалить контакт"')
        load()
        temp = ''
        if contact == []:
            update.message.reply_text(
                f'В телефонной книге отсутствуют контакты')
            cancel(update, _)
        else:
            for i in contact:
                temp += f'№{i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["coment"]})\n---------------------\n'
            update.message.reply_text(
                f'{temp}\nВведите № контакта для удаления')
            return DEL_CONT
    else:
        log.text_in_log('Я не понял, что он хотел от меня')
        update.message.reply_text('Я тебя не понимаю')
        cancel(update, _)


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    bot_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, message)],
        states={
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, surname)],
            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            TEL: [MessageHandler(Filters.text & ~Filters.command, tel)],
            COMMENT: [MessageHandler(Filters.text & ~Filters.command, comment)],
            SEARCH: [MessageHandler(Filters.text & ~Filters.command, search)],
            END_SEARCH: [MessageHandler(Filters.text & ~Filters.command, end_search)],
            DELETE_ALL: [MessageHandler(Filters.text & ~Filters.command, delete_all)],
            DEL_CONT: [MessageHandler(Filters.text & ~Filters.command, del_cont)],
            DEl_C: [MessageHandler(Filters.text & ~Filters.command, del_c)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(bot_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
