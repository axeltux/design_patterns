"""
    Implementación del patrón de diseño Prototype
"""
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}{self.value}: {self.value}"

# Crear una instancia del prototipo concreto 
prototype = ConcretePrototype("Prototipo ", 1)

# Clonar el prototipo
clone = prototype.clone()

# Cambiar el valor del clone
clone.value = 2

# Mostrar los valores de los dos prototipos
print(prototype)
print(clone)
