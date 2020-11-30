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


class Stock:
    full_stock = [(1, {'сканер': 'Canon Е400', 'цена': 4999.0, 'количество': 7}),
                  (2, {'принтер': 'HP LaserJet', 'цена': 14500.0, 'количество': 3}),
                  (3, {'ксерокс': 'Xerox 2135', 'цена': 18299.0, 'количество': 5}),
                  (4, {'сканер': 'Canon Е407', 'цена': 5000.0, 'количество': 2}),
                  (5, {'принтер': 'HP LaserJet2', 'цена': 12200.0, 'количество': 1}),
                  (6, {'ксерокс': 'Xerox 2715', 'цена': 17600.0, 'количество': 2}),
                  ]

    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    @staticmethod
    def choose_equ(num_a):
        if num_a == '1':
            b = 'принтер'
        elif num_a == '2':
            b = 'сканер'
        elif num_a == '3':
            b = 'копир'
        else:
            print('Ошибка ввода')

        mytemplate = {
            b: ('модель', str),
            'цена': ('стоимость товара', float),
            'количество': ('количество', int),
        }
        return mytemplate

    @staticmethod
    def choose_popping(num_c):
        if num_c == '1':
            c = 'принтер'
        elif num_c == '2':
            c = 'сканер'
        elif num_c == '3':
            c = 'копир'
        return c

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


print(f'Добро пожаловать в программу "Склад v1.01" \nПоследний актуальный релиз от 30.11.2020')
# можно внедрить выбора добавление нового склада, выбор из существующих складов

first_stock = Stock('"Хранитель-1"', 'г. Москва', 100)
print(f'Имя склада: {first_stock.name} Склад находится в {first_stock.location}')
stock_menu = True
while stock_menu:
    print('\n Главное меню. Выберите:')
    me_nu = input('Посмотреть склад - 1, Новое поступление - 2, Передать товар - 3, '
                  'Аналитика склада - 4, Завершить программу - 5\n')
    if me_nu not in ('1', '2', '3', '4', '5'):
        print('Неверный ввод, повторите выбор')
    if me_nu == '1':
        print('Раздел - 1. Посмотреть склад')
        print(*first_stock.full_stock, sep="\n")
    elif me_nu == '2':
        print('Раздел - 2. Новое поступление')
        next_enter = True
        next_num = 7
        while next_enter:
            new_item = {}
            a = input('Добавить новое поступление \nпринтер-1, сканер-2, копир-3, вернуться в меню - 4  ')
            if a == '4':
                break
            elif a in ('1', '2', '3'):
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
                next_add = input('Добавить новый продукт? да-1 нет-2? \n')
                if next_add in ('1', '2'):
                    next_enter = next_add == '1'
                    break
                else:
                    print('Ошибка! Неверный ввод.')
        else:
            print('Неверный ввод, повторите')
    elif me_nu == '3':
        print('-----Реализовать передачу товара со склада-----')
        print(*first_stock.full_stock, sep='\n')
        popping = input('Что вы хотите передать со склада в производство? Введите номер цифрой. \n'
                        'Если вы передумали удалять введите Enter')
        if popping == '':
            pass
        elif popping in ('0123456789'):
            # count_pises = input('Сколько штук?')
            # print("Эта функция будет реализована в след версии программы =)")
            zz = first_stock.full_stock.copy()
            zz.pop(int(popping)-1)
            print()
            print(*zz, sep='\n')

    elif me_nu == '4':
        print('Раздел - 4. Аналитика по складу')
        counting = []
        for items in first_stock.full_stock:
            for key in items[1].keys():
                if key == 'количество':
                    counting.append(items[1][key])
        sum_counting = sum(counting)
        free_places = first_stock.capacity - sum(counting)
        print(f'Общее количнство мест на складе: {first_stock.capacity} \n'
              f'Свободных мест: {free_places} \n')

        analytics = {}
        for item in first_stock.full_stock:
            for key, value in item[1].items():
                if key in analytics:
                    analytics[key].append(value)
                else:
                    analytics[key] = [value]
        print("Аналитика о товарах", *analytics.items(), sep="\n")

    elif me_nu == '5':
        print('Спасибо, было приятно поработать вместе. До новых встреч! \n'
              'Программа закончила работу.')
        break
