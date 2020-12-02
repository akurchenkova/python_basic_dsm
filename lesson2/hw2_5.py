"""
5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг: {my_list}')

while True:
    new_element = input('Введите целое число: ')
    if not new_element.isdigit():
        print("Ошибка. Еще раз: ")
    else:
        new_element = int(new_element)
        break

element_count = my_list.count(new_element)  # считаем, проверям, есть ли с таким значением элементы в рейтинге

# если нет то вставляем в начало/конец/середину рейтинга
if not element_count:
    if new_element > my_list[0]:
        my_list.insert(0, new_element)
    elif new_element < my_list[-1]:
        my_list.append(new_element)
    else:
        for index, item in enumerate(my_list):
            if item < new_element:
                my_list.insert(index, new_element)
                break
else:  # если элемент уже есть в рейтинге, то вставляем его на последнюю позицию среди подобных
    same_num = my_list.index(new_element) + element_count
    my_list.insert(same_num, new_element)

print(f'Текущий рейтинг: {my_list}')
