"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
# !использовала присланный файл

import os.path

info_file = os.path.join(os.path.dirname(__file__), 'text_4.txt')
file_new = os.path.join(os.path.dirname(__file__), 'text_4_new.txt')

nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    with open(info_file, 'r', encoding='UTF-8') as reading_f, open(file_new, 'w', encoding='UTF-8') as writing_f:
        for line in reading_f:
            try:
                num = line.split()[0]
                line = line.replace(num, nums.get(num))
                writing_f.write(line)
            except TypeError:
                print('Не все значения были перезаписаны, тк пропущены данные в исходном файле')
                continue

except FileNotFoundError:
    print('Файл text_4.txt в рабочей директории отсутсвует')
