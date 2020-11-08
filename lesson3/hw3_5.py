"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ q, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def funk_num_list(*args):
    """
    Функция возвращающая сумму для только что введеных чисел

    """
    tmp_num_list = []
    for char in sentence.split():
        if char.isdigit():
            tmp_num_list.append(int(char))
    my_sum = sum(tmp_num_list)
    return my_sum


all_sum = []
while True:
    sentence = input('Введите несколько чисел, разделенных пробелом '
                     'или введите q для выхода: ')
    if sentence.lower() == "q":
        print('Программа закончила работу')
        break
    else:
        mark = sentence.split()
        all_sum.append(funk_num_list(sentence))
        summa = sum(all_sum)
        print(summa)
        if 'q' in mark:
            print('Программа всё просуммировала и закончила работу')
            break