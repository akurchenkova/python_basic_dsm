"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

array = input("Введите числа списка через пробел: ").split(sep=' ')
print('Введеный список: ', array)

# if len(array) % 2 == 0:
#     idx = len(array)
# else:
#     idx = len(array) - 1
idx = len(array) if len(array) % 2 == 0 else len(array) - 1

array[:idx:2], array[1:idx:2] = array[1:idx:2], array[:idx:2]
print('Измененный список: ', array)