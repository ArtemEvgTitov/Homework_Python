# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию,
# которая спрашивает ключ, считывает текст и дешифровывает его.

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def encryption(key, alphabet):
    message = input("Введите сообщение для шифровки: ").upper()
    total = ''
    with open('task4_Seminar4.txt', 'w', encoding="utf-8") as data:
        for i in message:
            index = alphabet.find(i)
            new_index = index + key
            if i in alphabet:
                total += alphabet[new_index]
            else:
                total += i
        data.write(total)


def decryption(key, alphabet):
    total = ''
    temp = ''
    with open('task4_Seminar4.txt', 'r', encoding="utf-8") as data:
        for i in data:
            temp += i
        for i in temp:
            index = alphabet.find(i)
            new_index = index - key
            if i in alphabet:
                total += alphabet[new_index]
            else:
                total += i
    return total


process = input(
    "\nВыберите действие.\n  1 - шифрование;\n  2 - дешифрование.\nВаш выбор: ").upper()
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key_received = False
while key_received == False:
    key = InputNumbers("Введите ключ шифрования: ")
    key_received = True

if process == '1':
    encryption(key, alphabet)
elif process == '2':
    print(decryption(key, alphabet))
