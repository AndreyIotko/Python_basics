# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# with open('task_4.txt', encoding='utf-8') as my_file:
#     my_file_2 = open('task_4_1.txt', 'a', encoding='utf-8')
#     for line in my_file:
#         lst = line.split(' ', 1)
#         my_file_2.write(rus[lst[0]] + ' ' + lst[1])
#     my_file_2.close()


with open('task_4.txt', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split(' ', 1)
        with open('task_4_1.txt', 'a', encoding='utf-8') as my_file_2:
            my_file_2.write(rus[line[0]] + ' ' + line[1])
