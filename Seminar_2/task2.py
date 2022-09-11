# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

result = False
number = str(input('Введите число '))

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

while result == False:
    if number.isdigit() == False:
        number = str(input('Некорректный ввод. Введите число '))
    number_list = []
    for i in range(1, int(number) + 1):
        number_list.append(mult(i))
    result = True

print(f"Произведения чисел от 1 до {number}:  {number_list}")
