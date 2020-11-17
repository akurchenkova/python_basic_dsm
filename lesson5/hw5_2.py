# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
# !мой file2.txt приложен

import os.path

file2 = os.path.join(os.path.dirname(__file__), 'file2.txt')

try:
    with open(file2, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        words_count = [(idx, len(line.split())) for idx, line in enumerate(lines, 1)]
        print(f'Строк в файле: {len(lines)} \nКоличетство слов в каждой строке:')
        for i, el in words_count:
            print(f'{i}: {el}')
except FileNotFoundError:
    print('Файл file2.txt в рабочей директории отсутсвует')
