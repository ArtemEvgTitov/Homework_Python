# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.

# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

angela = ('Ангела Меркель', 5)
andrey = ('Андрей Валетов', 5)
freddy = ('Фредди Меркури', 3)
anastasiya = ('Анастасия Пономарева', 4)
score = 5

students_list = [angela, andrey, freddy, anastasiya]


def writing(list):
    with open('task3_Seminar4.txt', 'w', encoding="utf-8") as data:
        for i in list:
            data.write(f"{i}\n")


def change_letters(score):
    temp_list = []
    with open('task3_Seminar4.txt', 'r', encoding="utf-8") as data:
        for line in data:
            if str(score) in line:
                line = line.upper()
            temp_list.append(line)
    return temp_list


writing(students_list)
writing(change_letters(score))

