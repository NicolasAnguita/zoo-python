from clases import Animal

class Leon(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 100, 150)

