# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу


def my_func(el):
    """used with filter() function"""
    try:
        el = float(el)
    except ValueError:
        return False
    return True


result = []
cont = True
while cont:
    result += input('q - exit / Enter numbers separated by a space: ').upper().split()
    if 'Q' in result:
        result = result[:result.index('Q')]
        cont = False
    result = list(map(float, list(filter(my_func, result))))
    print(sum(result))
