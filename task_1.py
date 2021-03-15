# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys


def salary_emp(tot_h, rate_h, award):
    try:
        tot_h = float(tot_h)
        rate_h = float(rate_h)
        award = float(award)
    except ValueError:
        return 'Incorrectly specified data!'
    else:
        return round(tot_h * rate_h + award, 2)


try:
    total_h, rate, aw = sys.argv[1:]
except ValueError:
    print('Not all data entered! total hours / Rate per hour / Premium.')
else:
    print(salary_emp(total_h, rate, aw))
