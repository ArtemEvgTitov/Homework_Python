# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(number):
    positive_list_Fibonacci = [0, 1]
    negative_list_Fibonacci = [1, 0]
    index = 2
    Fibonacci_list = []
    
    while index <= number:
        positive_list_Fibonacci.append(positive_list_Fibonacci[index - 1] + positive_list_Fibonacci[index - 2])
        negative_list_Fibonacci.insert(0, positive_list_Fibonacci[index]*(-1))
        index += 1

    Fibonacci_list = negative_list_Fibonacci + positive_list_Fibonacci
    return Fibonacci_list

print(Fibonacci(8))