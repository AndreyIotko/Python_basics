# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету
# и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


with open('task_6.txt', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        subj, h = line.split(' ', 1)
        hours = []
        dig = ''
        for i in h:
            if i.isdigit():
                dig += i
            else:
                if dig != '':
                    hours.append(int(dig))
                    dig = ''
        my_dict[subj] = sum(hours)
    print(my_dict)

# import re
#
# with open('task_6.txt', encoding='utf-8') as f_obj:
#     my_dict = {}
#     for line in f_obj:
#         subj, hours = line.split(' ', 1)
#         my_dict[subj] = sum(list(map(int, re.findall(r"\d+", hours))))
#     print(my_dict)
