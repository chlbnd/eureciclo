from bottle import Bottle

class Gallon:

    def __init__(self, gallons):
        self.__gallons = gallons
        self.__liters = [gallons]

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
        liters = self.liters

        if liters in bottles.bottles:
            dump = bottles.dump(liters)
            self.__liters -= dump

        if liters > bottles.larger():
            dump = bottles.dump(bottles.larger())
            self.__liters -= dump

        if liters < bottles.smaller():
            dump = bottles.dump(bottles.smaller())
            self.__liters -= dump

        return dump