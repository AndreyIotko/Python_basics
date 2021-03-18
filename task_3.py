# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников

with open('task_3.txt') as f_obj:
    less_20 = []
    average = 0
    for line in f_obj:
        average += float(line.split()[1])
        if float(line.split()[1]) < 20000:
            less_20.append(line.split()[0])
    f_obj.seek(0)
    average = round(average / len(f_obj.readlines()), 2)
    print(f'Average salary = {average}')
    print(f'The surnames of employees who receive less than 20000 :{", ".join(less_20)}')
