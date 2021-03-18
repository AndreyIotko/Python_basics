# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open('task_1.txt', 'w', encoding='utf-8')
while True:
    text = input(':')
    if text == '':
        break
    f_obj.write(text + '\n')

f_obj.close()


# with open('task_1.txt', 'a', encoding='utf-8') as f:
#     while True:
#         text = input(':')
#         if text == '':
#             break
#         f.write(text + '\n')
