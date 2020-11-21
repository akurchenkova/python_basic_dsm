"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight():
    yellow_color = '\033[93m'
    red_color = '\033[31m'
    green_color = '\033[32m'
    nocolor = '\033[0m'

    def traffic_timer(self, start):
        for a in range(start, 0, -1):
            if a != 1:
                print(a, end=' ')
            else:
                print(a)
            time.sleep(1)

    def running(self, color):
        self.color = color
        if self.color == "red":
            print(self.red_color, "КРАСНЫЙ СИГНАЛ", self.nocolor)
            self.traffic_timer(7)
        elif self.color == "yellow":
            print(self.yellow_color, "ЖЕЛТЫЙ СИГНАЛ", self.nocolor)
            self.traffic_timer(2)
        elif self.color == "green":
            print(self.green_color, "ЗЕЛЕНЫЙ СИГНАЛ", self.nocolor)
            self.traffic_timer(9)
        else:
            print(f"Светофор сломался")


tr = TrafficLight()
# сломанный вариант
# traffic_lights = ['red', 'yellow', 'green', 'white', 'yellow']
# рабочий вариант
traffic_lights = ['red', 'yellow', 'green', 'yellow']
while traffic_lights == ['red', 'yellow', 'green', 'yellow']:
    for light in traffic_lights:
        tr.running(light)
else:
    print(f"Светофор сломался")
