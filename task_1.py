# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

while True:
    try:
        num_1 = float(input('Enter the first number :'))
        num_2 = float(input('Enter the second number :'))
    except ValueError:
        print('Value Error ! Not a digit entered')
    else:
        break


def divide(num, div):
    return round(num / div, 2) if div else 'Can not be divided by zero!'


print(divide(num_1, num_2))


