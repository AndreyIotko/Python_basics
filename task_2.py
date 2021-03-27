# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, par):
        self.param = par

    @abstractmethod
    def tissue_consumption(self):
        return 'Coat = (par/6.5 + 0.5),Costume = (2 * par + 0.3)'


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def tissue_consumption(self):
        return round(2 * self.param + 0.3, 1)


coat = Coat(25)
print(coat.tissue_consumption)
suit = Costume(25)
print(suit.tissue_consumption)
