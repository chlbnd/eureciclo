class Bottle:

    def __init__(self, bottles):
        self.__bottles = bottles
        self.__used = []

    @property
    def bottles(self):
        return self.__bottles

    @property
    def used(self):
        return self.__used.sort(reverse=True)

    def leftover(self, liters):
        return sum(self.__used) - liters

    def larger(self):
        return max(self.__bottles)

    def smaller(self):
        return min(self.__bottles)

    def dump(self, dump):
        self.__used.extend([dump])
        self.__bottles.remove(dump)
        return dump
