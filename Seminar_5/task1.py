# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

string_text = 'абвгдейка - это передача'
list_string = string_text.split()
for string in list_string:
    if 'абв' in string:
        list_string.remove(string)
string_total = ''
for string in list_string:
    string_total += string + ' '
print(string_total)