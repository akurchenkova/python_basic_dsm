"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, name, color, is_police):
        self.speed, self.name, self.color, self.is_police = speed, name, color, is_police


    def go(self):
        return f'{self.color} {self.name} поехала'

    def stop(self):
        return f'{self.color} {self.name} остановилась'

    def turn(self, direction):
        return f'{self.color} {self.name} повернула на {direction}'

    def show_speed(self):
        if self.is_police:
            return f'Полицейская {self.name} - {self.speed} км/ч'
        else:
            return f'{self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, name, color, is_police=False, limit=60):
        super().__init__(speed, name, color, is_police)
        self.limit = limit

    def show_speed(self):
        if self.speed > self.limit:
            return f'{self.name} превысила скорость на {self.speed - self.limit} км/ч'
        else:
            return f'{self.name} - {self.speed} км/ч'

class SportCar(Car):
    def __init__(self, speed, name, color, is_police=False):
        super().__init__(speed, name, color, is_police)

class WorkCar(Car):
    def __init__(self, speed, name, color, is_police=False, limit=40):
        super().__init__(speed, name, color, is_police)
        self.limit = limit

    def show_speed(self):
        if self.speed > self.limit:
            return f'{self.name} превысила скорость на {self.speed - self.limit} км/ч'
        else:
            return f'{self.name} - {self.speed} км/ч'

class PoliceCar(Car):
    def __init__(self, speed, name, color='голубая', is_police=True):
        super().__init__(speed, name, color, is_police)

town_car = TownCar(180, 'Toyota', 'зеленая')
print(town_car.turn('налево'), town_car.show_speed(), sep='\n')
sport_car = SportCar(240, 'Lamborghini', 'желтая')
print(sport_car.go(), sport_car.show_speed(), sep='\n')
work_car = WorkCar(0, 'Лада калина', 'белая')
print(work_car.stop(), work_car.show_speed(), sep='\n')
police_car = PoliceCar(80, 'Ford Focus')
print(police_car.go(), police_car.show_speed(), sep='\n')
print(police_car.is_police)
