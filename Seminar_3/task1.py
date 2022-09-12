# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_number = [2, 3, 5, 9, 3, 5, 7, 3, 9, 2] # 3 9 5 3 2 сумма 22

def sum_odd_numbers(list):
    index = 0
    sum_num = 0
    for i in list:
        if index % 2 != 0:
            sum_num += i
        index += 1
    return sum_num

print(sum_odd_numbers(list_number))