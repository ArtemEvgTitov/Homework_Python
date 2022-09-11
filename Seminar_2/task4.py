# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def random(max_number, min_number): 
  
     t_data = '%.9f' % time.time() 
     time.sleep(0.00001) 
     interval = max_number - min_number 
     razrad = len(str(interval)) * -1 
     smech = int(t_data[razrad:]) 
  
     while smech > interval: 
         smech = int(smech / 2) 
  
     rnd_num = min_number + smech 
     return rnd_num

number_ok = False
while number_ok == False:
    min_number = InputNumbers("Введите минимальное число ")
    max_number = InputNumbers("Введите максимальное число ")
    if min_number > max_number:
        print('Введите числа ещё раз')
    else:
        number_ok = True
        
rnd_number = random(max_number, min_number)
print(f'Случайное число равно {rnd_number}')
