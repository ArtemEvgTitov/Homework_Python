# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

list_number1 = [1.1, 1.2, 3.1, 5.17, 10.02]
list_number2 = [4.07, 5.1, 8.2444, 6.98]


def difference(list):
    temp_list = []
    for i in list:
        temp_list.append(i % 1)
    max_num = max(temp_list)
    min_num = min(temp_list)

    return round((max_num - min_num), 4)


print(difference(list_number1))
print(difference(list_number2))
