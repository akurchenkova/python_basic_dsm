"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from random import randrange

lst_o = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список", lst_o)
# for i in range(1, len(lst_o)):
#     if lst_o[i] > lst_o[i - 1]:
#         print([lst_o[i]])
print("Результат range", [lst_o[i] for i in range(1, len(lst_o)) if lst_o[i] > lst_o[i - 1]])

# for idx, el in enumerate(lst_o):
#     if idx and el > lst_o[idx - 1]:
#         print([el])
print("Результат enume", list(el for idx, el in enumerate(lst_o) if idx and el > lst_o[idx - 1]))

print("--- Рандомчик ---")
lst_r = [randrange(-10, 10) for a in range(13)]
print("Рандомный список №2", lst_r)
print("Результат range", [lst_r[i] for i in range(1, len(lst_r)) if lst_r[i] > lst_r[i - 1]])
print("Результат enume", list(el for idx, el in enumerate(lst_r) if idx and el > lst_r[idx - 1]))
