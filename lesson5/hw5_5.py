# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os.path
import random

file_path = os.path.join(os.path.dirname(__file__), 'file5.txt')

numbers = [random.randint(1, 100) for _ in range(random.randint(5, 20))]

with open(file_path, 'w', encoding='UTF-8') as file5:
    file5_line = ' '.join(map(str, numbers))
    file5.write(file5_line)
print('Сумма чисел в файле: ', sum(numbers))
