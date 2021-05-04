# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_info(name, surname, year, city, phone, email):
    return f'{name} {surname} {year} {city} {phone} {email}'


print(user_info(name='Alex', surname='Cross', year=1993, city='Moscow', phone=86247435, email='a.cross1993@gmail.com'))


def user_info_2(**kwargs):
    my_str = ''
    for val in kwargs.values():
        my_str += str(val) + ' '
    return my_str


print(user_info_2(name='Alex', surname='Cross', year=1993, city='Moscow', phone=86247435, email='a.cross1993@gmail.com'))
