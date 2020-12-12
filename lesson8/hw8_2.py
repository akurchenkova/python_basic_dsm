"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyOwnError(Exception):
    def __init__(self, message):
        self.message = message


while True:
    print('\n Программа находит значение выражения x/y.')
    print('Введите делимое')
    while True:
        x = input('x = ')
        tmp_x = x
        if '-' in tmp_x:
            tmp_x = tmp_x.strip('-')
        if tmp_x.isnumeric():
            x = float(x)
            break
        print('Ошибка ввода. Надо ввести число.')

    print('Введите делитель')
    while True:
        y = input('y = ')
        tmp_y = y
        if '-' in tmp_y:
            tmp_y = tmp_y.strip('-')
        if tmp_y.isnumeric():
            y = float(y)
            break
        print('Ошибка ввода. Надо ввести число.')
    try:
        if y == 0:
            raise MyOwnError('Делитель не может быть равен 0.')
        print(f'{x}/{y} = {x / y:.2f}')
    except ValueError:
        print('Ошибка: введено некорректное значение.')
    except MyOwnError as err:
        print(err)

    if input('\n Нажмите Enter для продолжения или любую клавишу для выхода...') != '':
        break
