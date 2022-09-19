# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - выиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

def InputCandies(inputText, max_candies): # Проверка хода игрока
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            while number < 1 or number > max_candies:
                print('Число введено некорректно')
                number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def InputNumbers(inputText): # Проверка введённого числа
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            while number < 1:
                print('Число введено некорректно')
                number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def Priority(player1, player2): # Жеребьёвка игроков
    gamer_list = [player1, player2]
    first = random.choice(gamer_list)
    for player in gamer_list:
        if first == player1:
            second = player2
        else:
            second = player1
    print(f'\nПервым(ой) ходит... {first}')
    print(f'После {first} ходит {second}')
    return first

def Rules_game(): # Правила игры
    total_number_candies = InputNumbers('\nВведите общее количество конфет: ')
    max_candies = InputNumbers('Введите максимальное количество конфет для хода: ')
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    return total_number_candies, max_candies, player1, player2

def player_move(player, total_number_candies, max_candies): # Ход Игрока
    move = InputCandies(f"\n{player}, введите количество конфет, которое возьмете от 1 до {max_candies}: ", max_candies)
    print(f"Ходил {player}, он взял {move}. Осталось на столе {total_number_candies - move} конфет.")
    return move

total_number_candies, max_candies, player1, player2 = Rules_game()
first = Priority(player1, player2)

while total_number_candies > max_candies:
    if first == player1:
        move = player_move(player1, total_number_candies, max_candies)
        total_number_candies -= move
        first = player2
    else:
        move = player_move(player2, total_number_candies, max_candies)
        total_number_candies -= move
        first = player1

if first == player1:
    print(f"\nВыиграл {player1}")
else:
    print(f"\nВыиграл {player2}")