# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

result = False
palin_list = list(input('Введите число '))
inverted_list = list(reversed(palin_list))

while result == False:
    if palin_list == inverted_list:
        print(f'Палиндром = {palindrome}')
        result = True
    else:
        palindrome = "".join(palin_list)
        inverted = "".join(inverted_list)
        palindrome = str(int(palindrome) + int(inverted))
        palin_list = list(palindrome)
        inverted_list = list(reversed(palin_list))