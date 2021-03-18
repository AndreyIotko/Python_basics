# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2.txt', encoding='utf-8') as file:
    print(f'There are {len(file.readlines())} lines in the file')
    file.seek(0)
    for i, line in enumerate(file, start=1):
        print('{} line contains {} word'.format(i, len(line.split())))
