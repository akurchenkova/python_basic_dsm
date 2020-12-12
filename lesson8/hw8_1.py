"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date
        Date.date = date
        if '.' in date:
            self.date = date.split('.')
        if '/' in date:
            self.date = date.split('/')
        self.date[0] = '{:02}'.format(int(self.date[0])) if len(self.date[0]) == 1 else self.date[0]
        self.date[1] = '{:02}'.format(int(self.date[1])) if len(self.date[1]) == 1 else self.date[1]
        self.date[2] = '{:04}'.format(int(self.date[2])) if len(self.date[2]) < 4 else self.date[2]
        self.date = '-'.join(self.date)
        print(f'Дата отформатирована {self.date}')

    def __str__(self):
        return self.date

    @classmethod
    def extract_data(cls):
        if '-' in cls.date:
            return map(int, cls.date.split('-'))
        if '.' in cls.date:
            return map(int, cls.date.split('.'))
        if '/' in cls.date:
            return map(int, cls.date.split('/'))

    @staticmethod
    def validate_data(day, month, year):
        checked = f'Дата сохранена'
        if year < 1 or len(str(year)) > 4:
            print('Ошибиться с годом было сложно, но у вас получилось')
        elif not 1000 < year < 3000:  # тут диапазон вариативен
            print('Ошибка в годе')
        elif not 1 <= month <= 12:
            print('Ошибка в месяце')
        elif month in [1, 3, 5, 7, 8, 10, 12] and not 1 <= day <= 31:
            print('Ошибка в этом месяце, нет столько дней')
        elif month in [4, 6, 9, 11] and not 1 <= day <= 30:
            print('Ошибка в этом месяце, нет столько дней')
        elif month == 2:
            if year % 4 or (year % 100 and year % 400):
                if not 1 <= day <= 29:
                    print('Ошибка в этом месяце в этом году, нет столько дней')
                print(checked)
            elif not 1 <= day <= 28:
                print('Ошибка в этом месяце в этом году, нет столько дней')
            else:
                print(checked)
        else:
            print(checked)


dates = []
while True:
    elem = input('Введите дату в формате dd-mm-yy или s для выхода: ')
    if elem == 's' or elem == 'ы' or elem == 'S':
        print('Сохраненные даты')
        print(*dates, sep='\n')
        break
    if elem == '':
        continue
    if elem in set('qweadzxcQWEADZXC'):  # буквы соседние с s
        continue
    try:
        elem = Date(elem)
        d, m, y = Date.extract_data()
        Date.validate_data(d, m, y)
        dates.append(elem)
    except Exception as err:
        print('Внимание ошибка: ', err, ' Данные не сохранены.')
