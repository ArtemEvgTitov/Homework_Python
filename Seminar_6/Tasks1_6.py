# 1- Определить, присутствует ли в заданном списке строк, некоторое число
# 2- Найти сумму чисел списка стоящих на нечетной позиции
# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# 1
print('\nTask 1')

# 2
print('\nTask 2')

list_task2 = [2, 3, 5, 9, 3, 5, 7, 3, 9, 2]  # 3 9 5 3 2 сумма 22
new_list = list(filter(lambda x: x[0] % 2 != 0, enumerate(list_task2)))
print(sum([n[1] for n in new_list]))

# 3
print('\nTask 3')

# 4
print('\nTask 4')

# 5
print('\nTask 5')

list_task5 = [2, 3, 4, 5, 6] # [12, 15, 16]
temp = list(map(lambda x, y: x * y, list(reversed(list_task5)), list_task5[:-2]))
print(temp)

# 6
print('\nTask 6')

N = 5
list_task6 = list(n for n in range(1, N))
list_task6 = list(map(lambda x: (-3) ** x, list_task6))
list_task6.insert(0, 1)
print(list_task6)
