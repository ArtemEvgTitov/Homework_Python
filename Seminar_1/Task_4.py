# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if quarter < 1 or quarter > 4:
    print('Такой четверти не существует')
    exit()
elif quarter == 1:
    range = '(x > 0; y > 0)'
elif quarter == 2:
    range = '(x < 0; y > 0)'
elif quarter == 3:
    range = '(x < 0; y < 0)'
elif quarter == 4:
    range = '(x > 0; y < 0)'
print(f'Диапозон возможных точек для {quarter} четверти {range}')