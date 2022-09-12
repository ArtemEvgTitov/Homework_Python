# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list_number = [2, 3, 4, 5, 6]

def pairs_of_numbers(list):
    start_index = 0
    end_index = len(list) - 1
    multiplication = []
    for i in list:
        if start_index > end_index:
            return multiplication
        multiplication.append(i*list[end_index])
        start_index += 1
        end_index -= 1

print(pairs_of_numbers(list_number))