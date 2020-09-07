class Response:
    def __init__(self, gallons, bottles):
        self.__gallons = gallons
        self.__bottles = bottles

    def build_response(self):
        gallons = self.gallons()
        bottles = self.bottles()
        leftover = self.leftover()
        response = f"{gallons}{bottles}{leftover}"
        return response

    def gallons(self):
        if self.__gallons == [0]:
            return "Como não havia nenhum galão, "

        if 1 == len(self.__gallons):
            return f"Um galão com a capacidade de {self.__gallons[0]} L foi preenchido "

        return f"Galões com a capacidade de {self.__gallons} L foram preenchidos "

    def bottles(self):
        if not self.__bottles or self.__gallons == [0]:
            return "nenhuma garrafa foi esvaziada"

        if 1 == len(self.__bottles):
            return f"por uma garrafa de {self.__bottles[0]} L"

        return f" pelas garrafas de {self.__bottles} L"

    def leftover(self):
        leftover = sum(self.__bottles) - sum(self.__gallons)

        if self.__gallons == [0] or leftover == 0:
            return "."

        if 0 > leftover:
            leftover *= -1
            return f", mantendo {round(leftover, 2)} L de capacidade livre."

        return f" com uma sobra de {leftover} L."