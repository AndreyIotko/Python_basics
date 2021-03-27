# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        my_str = ''
        for el in self.my_list:
            my_str += '    '.join(map(str, el)) + '\n'
        return my_str

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            for el in range(len(self.my_list)):
                for i in range(len(other.my_list[el])):
                    self.my_list[el][i] += other.my_list[el][i]
            return self
        else:
            return 'Error!\n'


matrix_1 = Matrix([[31, 22, 55, 77], [37, 43, 22, 54]])
print(matrix_1)

matrix_2 = Matrix([[22, 22], [32, 32], [11, 11]])
print(matrix_2)

matrix_3 = Matrix([[82, 93, 65, 34], [75, 61, 94, 76]])
print(matrix_3)

print(matrix_1 + matrix_2)

matrix_1 + matrix_3
print(matrix_1)
