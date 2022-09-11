# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

number = list(input('Введите число: '))
number_list = list(range(0, 10))
sum_num = 0
for i in number:
    if i in str(number_list):
        sum_num += int(i)
print(sum_num)