# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

time = input("Введите время в секундах :")

seconds = int(time)
minutes = seconds // 6
seconds %= 60
hour = minutes // 60
minutes %= 60

print(f'{hour}:{minutes}:{seconds}')
print(f'{hour} часов:{minutes} минут:{seconds} секунд')
