# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_func(a, b):
    """Функция с позиционными аргументами, выполняющая деление.
    При необходимости округляет до 3 знаков.

    """
    try:
        result = a / b
        return round(result, 3)
    except ZeroDivisionError:
        return "Допущена ошибка: на ноль делить нельзя!"


while True:
    try:
        num_a = float(input('Введите a: '))
    except ValueError:
        print('Вы ввели не число')
        continue
    break

while True:
    try:
        num_b = float(input('Введите b: '))
    except ValueError:
        print('Вы ввели не число')
        continue
    break

print(division_func(num_a, num_b))
