"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

num_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, num_list))  # вариант №1

print(reduce(lambda prev_el, el: prev_el * el, num_list))  # вариант №2
