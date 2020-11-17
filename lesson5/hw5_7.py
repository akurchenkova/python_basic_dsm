"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать файл,
вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
# !использовала присланный файл

import os.path
import json

data = os.path.join(os.path.dirname(__file__), 'text_7.txt')
j_data = os.path.join(os.path.dirname(__file__), 'text_77.json')
try:
    with open(data, 'r', encoding='UTF-8') as db:
        firms = {}
        for line in db:
            itm = line.split()
            proceeds, costs = itm[2], itm[3]
            if proceeds.isdigit() and costs.isdigit():
                firms[itm[0]] = itm[2:]
            else:
                print('Не все данные распознаны, ошибка в числовой инфрмации')
        try:
            for key, value in firms.items():
                firms[key] = int(value[0]) - int(value[1])
        except ValueError:
            print('Данные в исходном файле повреждены')
        try:
            mid_av = round(sum(val for val in firms.values() if val > 0) / sum(1 for val in firms.values() if val > 0),
                           2)
        except ZeroDivisionError:
            mid_av = 0
        finance = {'average_profit': mid_av}
        data_list = [firms, finance]
        print(data_list)
        with open(j_data, "w", encoding='UTF-8') as write_jf:
            json.dump(data_list, write_jf, ensure_ascii=False, indent=4)
except FileNotFoundError:
    print('Файл text_7.txt в рабочей директории отсутствует')
