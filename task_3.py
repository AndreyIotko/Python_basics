# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


while True:
    try:
        number = int(input('Введите номер месяца от 1 до 12 :'))
    except ValueError:
        print('Ввести нужно целое число!')
    else:
        if number in range(1, 13):
            break

# 1
seasons = {
    'Зима': (1, 2, 12),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}
for key, value in seasons.items():
    if number in value:
        print(key)
# 2
months = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
seasons = ('Зима', 'Весна', 'Лето', 'Осень')
for el in months:
    if number in el:
        print(seasons[months.index(el)])
        break
# 2.1
seasons = [('Зима', 1, 2, 12), ('Весна', 3, 4, 5), ('Лето', 6, 7, 8), ('Осень', 9, 10, 11)]
for el in seasons:
    if number in el:
        print(el[0])
        break
