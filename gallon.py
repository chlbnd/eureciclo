from bottle import Bottle
from itertools import combinations

class Gallon:

    def __init__(self, gallons):
        self.__gallons = gallons
        self.__liters = gallons

        if isinstance(gallons, list):
            self.__liters = sum(gallons)

    @property
    def gallons(self):
        return self.__gallons

    @property
    def liters(self):
        return self.__liters

    @liters.setter
    def liters(self, liters):
        self.__liters -= liters

    def fill(self, bottles: Bottle):
        comb_list = list()
        for idx in range(len(bottles.bottles)):
            comb_list.extend([comb for comb in combinations(bottles.bottles, idx + 1)])

        sum_list = list(map(sum, comb_list))

        liters = self.liters
        if liters in sum_list:
            idx = sum_list.index(liters)
            return sorted(comb_list[idx])

        delta = [(value - liters) for idx, value in enumerate(sum_list)]

        surplus = min([value for value in delta if value > 0])
        lack = min([abs(value) for value in delta if value < 0])

        if surplus <= lack:
            idx = delta.index(surplus)
            return comb_list[idx]

        idx = delta.index(lack * -1)
        return comb_list[idx]
