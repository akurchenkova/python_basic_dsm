"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
# ПРОЕКТ ЕЩЕ В РАЗРАБОТКЕ

class Stock:
    full_stock = [(1, {'сканер': 'Canon Е400', 'цена': 4999.0, 'количество': 7}),
                  (2, {'принтер': 'HP LaserJet', 'цена': 14500.0, 'количество': 3}),
                  (3, {'ксерокс': 'Xerox 2135', 'цена': 18299.0, 'количество': 5}),
                  ]

    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    @staticmethod
    def choose_equ(a):
        if a == '1':
            a = 'принтер'
        elif a == '2':
            a = 'сканер'
        else:
            a = 'копир'

        template = {
            a: ('модель', str),
            'цена': ('стоимость товара', float),
            'количество': ('количество', int),
        }
        return template


class Equipment:
    def __init__(self, title, price, size, out=False):
        self.title = title
        self.price = price
        self.size = size
        self.out = out



class Printer(Equipment):
    def __init__(self, title, price, size, out=False):
        super().__init__(title, price, size, out)
        self.printing = True


class Scanner(Equipment):
    def __init__(self, title, price, size, out=False):
        super().__init__(title, price, size, out)
        self.scanning = True


class Xerox(Equipment):
    def __init__(self, title, price, size, out=False):
        super().__init__(title, price, size, out)
        self.coping = True


first_stock = Stock('Хранитель-1', 'г. Москва', 1000)
print(f'Мест на складе: {first_stock.capacity}\nСклад находится в {first_stock.location}')

next_enter = True
next_num = 4

while next_enter:
    new_item = {}
    a = input('Добавить принтер-1, сканер-2, копир-3  ')
    template = Stock.choose_equ(a)
    for key, value in template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНеверное значение')
                continue
            new_item[key] = user_value
            break
    first_stock.full_stock.append((next_num, new_item))
    next_num += 1

    while True:
        next_add = input('Добавить еще продукт? да-Д нет-Н? \n')
        if next_add.lower() in ('д', 'н'):
            next_enter = next_add.lower() == 'д'
            break
        else:
            print('Неверный ввод, повторите')
print(first_stock.full_stock[:])
