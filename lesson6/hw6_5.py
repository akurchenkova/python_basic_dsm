"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self}')

    def __str__(self):
        return type(self).__name__


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой. Фирмы {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки карандашом. Фирмы {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки маркером. Фирмы {self.title}')


stati, pen, pencil, handle = Stationery(), Pen('Erich Krause'), Pencil('Faber-Castell'), Handle('Copic')

stati.draw(), handle.draw(), pen.draw(), pencil.draw()
