# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import random

N = random.randint(4, 1000)
print(f"\nЧисло N равно {N}")

def multipliers(N):
   i = 2
   multipliers = []
   while i * i <= N:
       while N % i == 0:
           multipliers.append(i)
           N = N / i
       i += 1
   if N > 1:
       multipliers.append(int(N))
   return multipliers

print(multipliers(N))