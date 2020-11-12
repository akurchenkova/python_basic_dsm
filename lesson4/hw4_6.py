"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
* использовать count() и cycle() совокупно в одном блоке кода
** всё выше + без break
"""

from sys import argv, exit
from itertools import count, cycle

script_name, start_num = argv

num_list = []
for el in count(int(start_num)):
    if el <= 10:
        num_list.append(el)
        print(el)
    else:
        print(num_list)
        y = int(start_num) * 2
        x = num_list
        for eli in cycle(x):
            if y >= len(num_list) * 3:
                exit("Закончили работу")
            else:
                print(eli)
                y += 1

# для ввода в терминал на mac
# python3 hw4_6.py 3
# cd /Users/akurchenkova/Documents/DSgbMed/Git/python_basic_dsm/lesson4/
