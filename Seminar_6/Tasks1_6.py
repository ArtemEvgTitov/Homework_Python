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

list_task1 = ['sdf', 'werwe', '2', 'rewq']
list_task1 = True in [n.isdigit() for n in list_task1]
print(list_task1)

# 2
print('\nTask 2')

list_task2 = [2, 3, 5, 9, 3, 5, 7, 3, 9, 2]  # 3 9 5 3 2 сумма 22
list_task2 = list(filter(lambda x: x[0] % 2 != 0, enumerate(list_task2)))
print(sum([n[1] for n in list_task2]))

# 3
print('\nTask 3')
import math

numbers = '5 1 2 1'
list_task3 = [float(n) for n in list(numbers.replace(" ", ""))]
sq = lambda x2, x1: (x2-x1)**2
print(round(math.sqrt((sq(list_task3[2], list_task3[0]) + sq(list_task3[3], list_task3[1]))), 2))

# 4
print('\nTask 4')

st = 2
list_task4 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
try:
    list_task4 = list(filter(lambda x: x, enumerate(list_task4)))
    temp = [n[0] for n in list_task4 if n[1] == st]
    print(temp[1])
except IndexError:
    print(-1)

# 5
print('\nTask 5')

list_task5 = [2, 3, 4, 5, 6]  # [12, 15, 16]
size = int(len(list_task5) / 2)
temp = list(
    map(lambda x, y: x * y, list(reversed(list_task5)), list_task5[:-size]))
print(temp)

# 6
print('\nTask 6')

N = 5
list_task6 = list(n for n in range(1, N))
list_task6 = list(map(lambda x: (-3) ** x, list_task6))
list_task6.insert(0, 1)
print(list_task6)
