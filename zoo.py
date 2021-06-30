#aqui comienza la tarea

#En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. Dele a cada animal diferentes niveles predeterminados de salud y felicidad.
#Los animales también deben responder al método de alimentación con diferentes niveles de cambios en la salud y la felicidad.

#from .clases.animal import Animal
from clases import Leon
from clases import Oso
from clases import Tigre

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animales(self, animal):
        self.animals.append(animal)
        return self


zoo1 = Zoo("ZooooLogico")

Yogui = Oso("Yogi", 25)
Minino = Tigre("Minino", 9)
Leoncio = Leon("Leoncio", 30)

zoo1.add_animales(Yogui).add_animales(Minino).add_animales(Leoncio)

for a in zoo1.animals:
    a.display_info()
