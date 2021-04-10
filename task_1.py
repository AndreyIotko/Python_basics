# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

number = 6
name = 'Lex'
floating = 2.25
said = True
print(number)
print(type(number))
print(name)
print(type(name))
print(floating)
print(type(floating))
print(said)
print(type(said))

input_name = input('Введите имя :')
input_age = int(input('Введите возраст :'))

print(f'{input_name} вам {input_age} лет')
