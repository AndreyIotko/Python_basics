# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [15, 13, 13, 13, 9, 9, 7, 5, 3, 3, 1]
print(rating_list)
while True:
    try:
        new_el = int(input('Enter a new rating :'))
    except ValueError:
        print('Enter an integer!')
    else:
        break

# rating_list.append(new_el)
# rating_list.sort(reverse=True)

if new_el <= rating_list[-1]:
    rating_list.append(new_el)
elif new_el in rating_list:
    rating_list.insert(rating_list.index(new_el), new_el)
elif new_el > rating_list[0]:
    rating_list.insert(rating_list.index(rating_list[0]), new_el)
    # rating_list = [new_el] + rating_list
else:
    for ind in range(len(rating_list) - 1):
        if new_el > rating_list[ind + 1]:
            rating_list.insert(ind + 1, new_el)
            break

print(rating_list)
