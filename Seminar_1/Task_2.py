# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(x):
        list.append(input(f"Введите значение {xyz[i]}: "))
    return list

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")