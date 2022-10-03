import logger as log
from settings import TOKEN
import random
import json
import move_bot as mb
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


TOTAL, MOVE = range(2)


def start(update, _):
    log.log_one_argument('---ЗАПУСК БОТА---')
    reply_keyboard = [['20','30'], ['40','50'], ['60','70'], ['/info']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        'Сыграем? 😈'
        '\nКоманда /cancel, чтобы прекратить разговор.\n\n'
        'Выбери или введи общее количество кофет 🍬',
        reply_markup=markup_key,)
    return TOTAL


def info(update, context):
    log.log_one_argument('Вызвана справка')
    context.bot.send_message(
        update.effective_chat.id, '\n📓Условие: На столе лежит заданное в начале игроком общее количество конфет🍬\n\nПервый ход определяется жеребьёвкой.\n\nЗа один ход можно забрать не более заданного в начале игроками количества конфет.\n\nТот, кто берет последнюю конфету - \nВЫИГРАЛ 🤓')


def save():
    with open("regulations.json", "w", encoding="utf-8") as reg:
        reg.write(json.dumps(regulations, ensure_ascii=False))


def load():
    global regulations
    with open("regulations.json", "r", encoding="utf-8") as reg:
        regulations = json.load(reg)


def total_candy(update, _):
    load()
    regulations["total"] = int(update.message.text)
    reply_keyboard = [['2','3'], ['4','5'], ['6','7']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        'Сколько всего конфет можно взять за 1 ход?',
        reply_markup=markup_key,)
    return MOVE


def move_candy(update, _):
    regulations["move"] = int(update.message.text)
    regulations["player"] = update.message.chat.username
    save()
    log.log_two_argument('Правила определены', f'{regulations}')
    update.message.reply_text(
        f'Итак, правила определены:\n\nОбщее кол-во конфет - {regulations["total"]}\nМаксимум можно взять за ход - {regulations["move"]}\n\nДля начала игры введи - /game')
    return ConversationHandler.END


def cancel(update, _):
    log.log_one_argument('Выход из игры')
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def Priority(regulations):
    gamer_list = [regulations["player"], regulations["bot"]]
    first = random.choice(gamer_list)
    for player in gamer_list:
        if first == regulations["player"]:
            second = regulations["bot"]
        else:
            second = regulations["player"]
    log.log_one_argument(f'Первым ходил {first}')
    return first


def move_pl(update, context):
    load()
    arg = context.args
    if not arg:
        log.log_one_argument(f'Нет аргументов для {update.message.text}')
    elif int(arg[0]) > regulations["move"] or int(arg[0]) <= 0:
        log.log_two_argument(f'Игрок пытался обмануть меня', f'{regulations["player"]}: {update.message.text}')
        update.message.reply_text(f'Минимальное количество конфет - 1\n\nМаксимальное количество конфет - {regulations["move"]}')
    else:
        regulations["total"] -= int(arg[0])
        log.log_one_argument(f'Игрок забрал {int(arg[0])} конфет')
        if regulations["total"] <= 0:
            update.message.reply_text(f'{regulations["player"]} ВЫИГРАЛ')
            log.log_one_argument(f'{regulations["player"]} ВЫИГРАЛ')
            log.log_one_argument('---GAME OVER---')
            exit()
        move = mb.bot_move(regulations)
        regulations["total"] -= move
        if regulations["total"] <= 0:
            update.message.reply_text(f'{regulations["bot"]} ВЫИГРАЛ')
            log.log_one_argument(f'{regulations["bot"]} ВЫИГРАЛ')
            log.log_one_argument('---GAME OVER---')
            exit()
        update.message.reply_text(
            f'{regulations["bot"]} взял {move} конфет. \n\nОсталось {regulations["total"]} конфет')
        log.log_one_argument(f'{regulations["bot"]} взял {move} конфет')
        save()


def game(update, _):
    load()
    first = Priority(regulations)
    update.message.reply_text(f'Первым ходит... {first}')
    if first == 'T-1000':
        move = mb.bot_move(regulations)
        regulations["total"] -= move
        update.message.reply_text(
            f'{regulations["bot"]} взял {move} кофет. \n\nОсталось {regulations["total"]} конфет')
        log.log_one_argument(f'{regulations["bot"]} взял {move} конфет')
        save()

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TOTAL: [MessageHandler(Filters.text & ~Filters.command, total_candy)],
            MOVE: [MessageHandler(Filters.text & ~Filters.command, move_candy)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    info_handler = CommandHandler('info', info)
    game_handler = CommandHandler('game', game)
    move_handler = CommandHandler('move', move_pl)

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(move_handler)
    dispatcher.add_handler(game_handler)

    updater.start_polling()
    updater.idle()
