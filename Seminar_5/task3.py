# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: 
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, 
# его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&



def total(first_list, second_list):
    temp = []
    for string in first_list:
        temp.append(string.upper())
    total_list = list(zip(second_list, temp))
    return total_list

def unicode(total_list):
    temp = []
    for string in total_list:
        for s in string[1]:
            temp.append(ord(s))
        sum_string = sum(temp, 0)
        temp_string = (sum_string, string[1])
        temp.clear()
        if sum_string % string[0] == 0 and string[0] != 1:
            total_list[total_list.index(string)] = temp_string
        elif sum_string % string[0] != 0:
            total_list.remove(string)
    print(total_list)
            

first_list = ['python', 'c#', 'java']
second_list = range(1, len(first_list) + 1)
total_list = total(first_list, second_list)

print(total_list)
unicode(total_list)
