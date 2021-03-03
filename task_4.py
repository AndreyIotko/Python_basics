# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое длинное число :'))

max_numeral = 1

while number > 1:
    numeral = number % 10
    number //= 10
    if max_numeral < numeral:
        max_numeral = numeral
else:
    print(max_numeral)
