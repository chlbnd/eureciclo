class Bottle:

    def __init__(self, bottles):
        self.__bottles = bottles

    @property
    def bottles(self):
        return self.__bottles

    def larger(self):
        return max(self.__bottles)

    def smaller(self):
        return min(self.__bottles)

    def dump(self, dump):
        self.__bottles.remove(dump)
        return dump
