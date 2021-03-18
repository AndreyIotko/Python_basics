# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('task_5.txt', 'w+') as f:
    f.write(input('Enter numbers separated by a space :'))
    f.seek(0)
    try:
        print(sum(map(float, f.read().split())))
    except ValueError:
        print('Not numbers')
