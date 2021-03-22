# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        for i in cycle(self.__color):
            print(i)
            if i == 'red':
                sleep(7)
            elif i == 'yellow':
                sleep(2)
            else:
                sleep(5)


traffic = TrafficLight()
traffic.running()
