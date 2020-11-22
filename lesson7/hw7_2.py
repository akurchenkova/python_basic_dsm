"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name


class Overcoat(Clothes):
    def __init__(self, v):
        super().__init__(self)
        self.v = v

    def consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, h):
        super().__init__(self)
        self.h = h

    @property
    def consumption(self):
        return round(2 * self.h + 0.3, 2)


volume = 42
height = 1.75
oc, s = Overcoat(volume), Suit(height)
print(f'Расход ткани на пальто {volume} размера = {oc.consumption()} м')
print(f'Расход ткани на костюм на рост {height} = {s.consumption} м')
print(f'Общий расход ткани = {oc.consumption() + s.consumption} м')
