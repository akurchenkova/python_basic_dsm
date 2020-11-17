# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os.path

file1 = os.path.join(os.path.dirname(__file__), 'file1.txt')

with open(file1, 'w', encoding='UTF-8') as file:
    while True:
        line = input('Введите данные: ')
        if not len(line):
            break
        file.write(f'{line}\n')
