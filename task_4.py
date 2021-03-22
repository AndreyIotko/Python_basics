# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'The {self.name} has stopped.'

    def turn(self, direction):
        return f'The {self.name} turned {direction}.'

    def show_speed(self):
        return f'speed = {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        return f'speed = {self.speed}. You exceeded the speed!' if self.speed > 60 else f'speed = {self.speed}.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'speed = {self.speed}. You exceeded the speed!' if self.speed > 40 else f'speed = {self.speed}.'


class PoliceCar(Car):
    pass


town_car = TownCar(66, 'black', 'TownCar')
sport_car = SportCar(197, 'red', 'SportCar')
worker_car = WorkCar(41, 'green', 'WorkCar')
police_car = PoliceCar(155, 'white', 'PoliceCar', True)

print(sport_car.color)
print(police_car.is_police)
print(town_car.name)
print(worker_car.speed)

print(town_car.go(), town_car.turn('left'), town_car.show_speed(), town_car.turn('right'), town_car.stop())
print(sport_car.go(), sport_car.turn('left'), sport_car.stop(), sport_car.show_speed())
print(worker_car.go(), worker_car.turn('left'), worker_car.stop(), worker_car.show_speed())
print(police_car.go(), police_car.turn('left'), police_car.stop(), police_car.show_speed())
