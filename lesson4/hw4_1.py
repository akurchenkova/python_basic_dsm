"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# python3 hw4_1.py 170.5 1700 13000  данные для копирования (на mac!) и ввода в терминал
# зп брутто: ((выработка в часах * ставка в час) + премия) + (22 + 2,9 + 5,1 + 0,2)% от первой части
# зп нетто: ((выработка в часах * ставка в час) + премия) - 13%

from sys import argv


def funk_estimation(a, b, c):
    return a * b + c


try:
    _, working_hours, rate_in_hours, bonus = argv

    estimation = funk_estimation(float(working_hours), float(rate_in_hours), float(bonus))
    social_contributions = 22 + 2.9 + 5.1 + 0.2

    salary_bru = estimation + (estimation * social_contributions / 100)
    salary_net = estimation - estimation * 0.13
    tax = salary_bru - salary_net

    print(f"Вы думали, что зарабываете {salary_net} деревянных рубликов?")
    print(f"На самом деле вот сколько: {salary_bru} рублей.")
    print(tax, 'рублей отдано государству различными налогами за бесплатную медицину и возможно пенсию, если...')
except ValueError as err:
    print(f'Внимание ошибка. Данные повреждены. Чинить тут: {err}')
