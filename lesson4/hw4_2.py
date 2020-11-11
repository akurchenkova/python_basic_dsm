"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randrange

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список", original_list)
print("Результат", [original_list[i] for i in range(1, len(original_list)) if original_list[i] > original_list[i - 1]])

random_list = [randrange(-10, 10) for _ in range(13)]
print("Рандомный список", random_list)
print("Результат", [random_list[i] for i in range(1, len(random_list)) if random_list[i] > random_list[i - 1]])
