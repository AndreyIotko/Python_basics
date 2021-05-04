# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(my_list))
    return sum(my_list)


def my_func_1(*args):
    args = sorted(args)
    return args[-1] + args[-2]
