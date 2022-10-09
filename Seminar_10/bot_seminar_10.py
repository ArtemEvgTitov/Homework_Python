import logger as log
from settings import TOKEN
import json
import operator
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

SURNAME, NAME, TEL, COMMENT, SEARCH, END_SEARCH, DELETE_ALL, DEL_CONT, DEl_C, EDIT, EDITOR, EDIT_SURNAME, EDIT_NAME, EDIT_TEL, EDIT_COMMENT = range(
    15)

tel_numb = {"id": 0, "surname": '', "name": '', "tel": '', "comment": ''}
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
        sorted(contact, key=operator.itemgetter('surname', 'name'))
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
    reply_keyboard = [['Создать контакт', 'Изменить контакт'], [
        'Поиск', 'Все контакты'], ['Удалить все контакты', 'Удалить контакт']]
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
    try:
        if (update.message.text).isalpha() == False:
            log.text_in_log(
                f"Некорректный ввод фамилии - {update.message.text}")
            update.message.reply_text(
                'Фамилия введена некорректно. Повторите ввод\n/cancel')
            return SURNAME
        tel_numb['surname'] = (update.message.text).capitalize()
        save()
        log.text_in_log(f"Введена фамилия - {update.message.text}")
        update.message.reply_text('Введите имя\n/cancel')
        return NAME
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def name(update, _):
    try:
        if (update.message.text).isalpha() == False:
            log.text_in_log(f"Некорректный ввод имени - {update.message.text}")
            update.message.reply_text(
                'Имя введено некорректно. Повторите ввод\n/cancel')
            return NAME
        tel_numb['name'] = (update.message.text).capitalize()
        save()
        log.text_in_log(f"Введено имя - {update.message.text}")
        update.message.reply_text('Введите номер телефона без +\n/cancel')
        return TEL
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def tel(update, _):
    try:
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
        update.message.reply_text('Введите комментарий к контакту\n/cancel')
        return COMMENT
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def comment(update, _):
    try:
        tel_numb['comment'] = update.message.text
        save()
        log.text_in_log(f"Введён комментарий - {update.message.text}")
        add_contact(tel_numb)
        start(update, _)
        return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def search(update, _):
    try:
        log.text_in_log('Запущен поиск')
        text = update.message.text
        reply_keyboard = [['Да', 'Нет']]
        markup_key = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        temp = []
        load()
        for i in contact:
            if text.lower() in i["surname"].lower() or text in i["name"].lower() or text in i["tel"]:
                temp.append(i)
        for i in temp:
            update.message.reply_text(
                f'{i["surname"]} {i["name"]} тел. {i["tel"]} - {i["comment"]}\n',
                reply_markup=markup_key,)
        if temp == []:
            update.message.reply_text(
                'Я такого не нашёл :(', reply_markup=markup_key,)
            log.text_in_log('Поиск не дал результатов')
        update.message.reply_text('Повторить поиск?\n/cancel')
        return END_SEARCH
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def end_search(update, _):
    try:
        text = update.message.text
        if text == 'Нет':
            log.text_in_log('Отмена повторного поиска')
            start(update, _)
            return ConversationHandler.END
        elif text == 'Да':
            log.text_in_log('Повторный поиск')
            update.message.reply_text('Введите данные для поиска\n/cancel')
            return SEARCH
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def all_cont(update, _):
    load()
    temp = ''
    if contact == []:
        log.text_in_log('Контакты отсуствуют')
        update.message.reply_text('Контакты отсуствуют')
    else:
        for i in contact:
            temp += f'{i["surname"]} {i["name"]} тел. {i["tel"]} ({i["comment"]})\n---------------------\n'
        update.message.reply_text(temp)
        log.text_in_log('Вывод всех контактов на экран')
    start(update, _)


def delete_all(update, _):
    try:
        text = update.message.text
        if text == 'Да':
            path = 'contacts.json'
            f = open(path, 'w', encoding="utf-8")
            f.write('')
            f.close()
            update.message.reply_text('Все контакты удалены')
            log.text_in_log('Все контакты удалены')
        start(update, _)
        if text == 'Нет':
            cancel(update, _)
        return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def del_cont(update, _):
    try:
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
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def del_c(update, _):
    try:
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
            log.text_in_log(
                f'Удалён контакт {tel_num["surname"]} {tel_num["name"]}')
            update.message.reply_text('Готово')
            start(update, _)
        if text == 'Нет':
            cancel(update, _)
        return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def edit(update, _):
    try:
        load()
        text = int(update.message.text) - 1
        temp = {}
        for i in contact:
            if text == i['id']:
                temp = i
        with open("tel_numb.json", "w", encoding="utf-8") as tel:
            tel.write(json.dumps(temp, ensure_ascii=False))
        reply_keyboard = [['Имя', 'Фамилия'],
                          ['Номер телефона', 'Комментарий']]
        markup_key = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(
            'Что хотели бы изменить?\n/cancel', reply_markup=markup_key,)
        return EDITOR
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def editor(update, _):
    try:
        text = update.message.text
        if text == 'Имя':
            update.message.reply_text(
                'Введите новое имя для контакта\n/cancel')
            return EDIT_NAME
        elif text == 'Фамилия':
            update.message.reply_text(
                'Введите новую фамилию для контакта\n/cancel')
            return EDIT_SURNAME
        elif text == 'Номер телефона':
            update.message.reply_text(
                'Введите новый телефон для контакта\n/cancel')
            return EDIT_TEL
        elif text == 'Комментарий':
            update.message.reply_text(
                'Введите новый комментарий для контакта\n/cancel')
            return EDIT_COMMENT
        else:
            update.message.reply_text(
                f'В контактах отсутствут поле {text}. Повторите ввод\n/cancel')
            return EDITOR
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def edit_surname(update, _):
    try:
        if (update.message.text).isalpha() == False:
            log.text_in_log(
                f"Некорректный ввод фамилии - {update.message.text}")
            update.message.reply_text(
                'Фамилия введена некорректно. Повторите ввод\n/cancel')
            return EDIT_SURNAME
        else:
            with open("tel_numb.json", "r", encoding="utf-8") as tel:
                tel_numb = json.load(tel)
            tel_numb["surname"] = update.message.text
            save()
            load()
            for i in contact:
                if i["id"] == tel_numb["id"]:
                    log.text_in_log(
                        f'В контакте {i["surname"]} {i["name"]} изменена фамилия на {tel_numb["surname"]}')
                    i["surname"] = tel_numb["surname"]
            with open("contacts.json", "w", encoding="utf-8") as cont:
                cont.write(json.dumps(contact, ensure_ascii=False))
            update.message.reply_text('Готово')
            start(update, _)
            return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def edit_name(update, _):
    try:
        if (update.message.text).isalpha() == False:
            log.text_in_log("Некорректный ввод имени - {update.message.text}")
            update.message.reply_text(
                'Имя введено некорректно. Повторите ввод\n/cancel')
            return EDIT_NAME
        else:
            with open("tel_numb.json", "r", encoding="utf-8") as tel:
                tel_numb = json.load(tel)
            tel_numb["name"] = update.message.text
            save()
            load()
            for i in contact:
                if i["id"] == tel_numb["id"]:
                    log.text_in_log(
                        f'В контакте {i["surname"]} {i["name"]} изменено имя на {tel_numb["name"]}')
                    i["name"] = tel_numb["name"]
            with open("contacts.json", "w", encoding="utf-8") as cont:
                cont.write(json.dumps(contact, ensure_ascii=False))
            update.message.reply_text('Готово')
            start(update, _)
            return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def edit_tel(update, _):
    try:
        if (update.message.text).isdigit() == False:
            log.text_in_log(
                f"Некорректный ввод номера телефона - {update.message.text}")
            update.message.reply_text(
                'Номер введён неверно. Повторите ввод\n/cancel')
            return EDIT_TEL
        else:
            with open("tel_numb.json", "r", encoding="utf-8") as tel:
                tel_numb = json.load(tel)
            tel_numb["tel"] = update.message.text
            save()
            load()
            for i in contact:
                if i["id"] == tel_numb["id"]:
                    log.text_in_log(
                        f'В контакте {i["surname"]} {i["name"]} изменен номер телефона на {tel_numb["tel"]}')
                    i["tel"] = tel_numb["tel"]
            with open("contacts.json", "w", encoding="utf-8") as cont:
                cont.write(json.dumps(contact, ensure_ascii=False))
            update.message.reply_text('Готово')
            start(update, _)
            return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def edit_comment(update, _):
    try:
        with open("tel_numb.json", "r", encoding="utf-8") as tel:
            tel_numb = json.load(tel)
        tel_numb["comment"] = update.message.text
        save()
        load()
        for i in contact:
            if i["id"] == tel_numb["id"]:
                log.text_in_log(
                    f'В контакте {i["surname"]} {i["name"]} изменен комментарий')
                i["comment"] = tel_numb["comment"]
        with open("contacts.json", "w", encoding="utf-8") as cont:
            cont.write(json.dumps(contact, ensure_ascii=False))
        update.message.reply_text('Готово')
        start(update, _)
        return ConversationHandler.END
    except:
        update.message.reply_text(
            'Что-то пошло не так')
        cancel(update, _)


def message(update, _):
    text = update.message.text
    if text == 'Создать контакт':
        log.text_in_log('Нажата кнопка "Создать контакт"')
        update.message.reply_text(
            'Для отмены введите /cancel\n\nВведите фамилию')
        return SURNAME
    elif text == 'Изменить контакт':
        log.text_in_log('Нажата кнопка "Изменить контакт"')
        load()
        temp = ''
        if contact == []:
            update.message.reply_text(
                f'В телефонной книге отсутствуют контакты')
            cancel(update, _)
        else:
            for i in contact:
                temp += f'id: {i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["comment"]})\n---------------------\n'
            update.message.reply_text(
                f'{temp}\nВведите id контакта для изменения')
            return EDIT
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
                temp += f'id: {i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["comment"]})\n---------------------\n'
            update.message.reply_text(
                f'{temp}\nВведите id контакта для удаления')
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
            EDIT: [MessageHandler(Filters.text & ~Filters.command, edit)],
            EDITOR: [MessageHandler(Filters.text & ~Filters.command, editor)],
            EDIT_SURNAME: [MessageHandler(Filters.text & ~Filters.command, edit_surname)],
            EDIT_NAME: [MessageHandler(Filters.text & ~Filters.command, edit_name)],
            EDIT_TEL: [MessageHandler(Filters.text & ~Filters.command, edit_tel)],
            EDIT_COMMENT: [MessageHandler(Filters.text & ~Filters.command, edit_comment)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(bot_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
