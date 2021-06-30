#Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad
class Animal:

    def __init__(self, nombre, edad, salud = 100, felicidad = 100):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

#La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal.
    def display_info(self):
        print(f"El animal {self.nombre} tiene salud {self.salud} y felicidad {self.felicidad} ")
        return self

#También debe tener un método de alimentación que aumente la salud y la felicidad en 10.
    def alimentacion(self):
        self.salud +=10
        self.felicidad +=10
        return self

# larry = Animal("Larry", 23, 80, 90)
# larry.display_info().alimentacion().display_info()




