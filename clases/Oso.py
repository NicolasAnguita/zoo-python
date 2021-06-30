from clases import Animal

class Oso(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 80, 60)
