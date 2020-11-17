# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# !использовала присланный файл

import os.path

file3 = os.path.join(os.path.dirname(__file__), 'text_3.txt')

try:
    print('Сотрудники, чей доход < 20 тыс:')
    min_sum = float(20000)
    data_summa = 0
    idx = 0
    with open(file3, 'r', encoding='UTF-8') as f:
        for line in f:
            data = line.split()
            try:
                data[1] = float(data[1])
                if data[1] < min_sum:
                    print(f' {data[0]} {data[1]}')
                idx += 1
                data_summa += data[1]
            except (ValueError, IndexError):
                continue

        mid_average = data_summa / idx
        print(f'Средний доход сотрудников всего предприятия: {mid_average}')
except FileNotFoundError:
    print('Файл text_3.txt в рабочей директории отсутсвует')
