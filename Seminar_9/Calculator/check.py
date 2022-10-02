import logger as log


def check_number(text):
    try:
        a = float(text[0])
        b = float(text[1])
    except ValueError:
        log.log_two_argument('Ошибка при вводе чисел',
                             f'Пользователь ввёл: {text}')
        a, b = list(text[0]), list(text[1])
        for index, i in enumerate(a):
            if i.isdigit() == False:
                a[index] = '.'
        for index, i in enumerate(b):
            if i.isdigit() == False:
                b[index] = '.'
        a = float(''.join(a))
        b = float(''.join(b))
        log.log_one_argument(f'Исправил на: {a} и {b}')
    return a, b
