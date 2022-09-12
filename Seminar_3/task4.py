# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def Binary(n):  # Без рекурсии
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def Binary2(number: int, osn: int = 2, binary: str = '') -> str:  # При помощи рекурсии
    if number != 0:
        binary += Binary2(number // osn, osn, binary) + str(number % osn)
    return binary


print(Binary(45))
print(Binary2(45))
