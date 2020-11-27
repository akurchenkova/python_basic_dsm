"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{"+" if self.b >= 0 else ""}{self.b}i'

    def __add__(self, other):
        if not isinstance(other, MyComplexNumber):
            raise ValueError
        return MyComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if not isinstance(other, MyComplexNumber):
            raise ValueError
        return MyComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


CNum_1 = MyComplexNumber(5, 6)
print('Комлексное число 1: ', CNum_1)
CNum_2 = MyComplexNumber(7, -1)
print('Комлексное число 2: ', CNum_2)
CNum_3 = CNum_1 + CNum_2
print('Результат сложения комплексных чисел: ', CNum_3)
CNum_4 = CNum_1 * CNum_2
print('Результат умножения комплексных чисел: ', CNum_4)
