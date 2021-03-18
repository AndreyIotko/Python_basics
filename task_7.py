# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

with open('task_7.txt') as f_txt:
    average = 0
    my_list = []
    my_dict = {}
    num = 0
    for line in f_txt:
        firm, form, profit, costs = line.split()
        profit = float(profit) - float(costs)
        my_dict[firm] = profit
        if profit > 0:
            num += 1
            average += profit
    my_list.append(my_dict)
    my_list.append({'average_profit': round(average / num, 2)})
    with open('task_7_1.json', 'w') as f_json:
        json.dump(my_list, f_json)
    print(f'Created a json file with the following content \n{json.dumps(my_list)}')
