"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
# !использовала присланный файл

import os.path

data = os.path.join(os.path.dirname(__file__), 'text_6.txt')

db_dict = {}
try:
    with open(data, 'r', encoding='UTF-8') as data_f:
        for line in data_f:
            tmp = line.split(' ')
            data_key = tmp[0].replace(':', '')
            db_dict[data_key] = tmp[1:]
    # print(db_dict)
    result = {}
    for key, value in db_dict.items():
        result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])
    print(result)
except FileNotFoundError:
    print('Файл text_6.txt в рабочей директории отсутсвует')
