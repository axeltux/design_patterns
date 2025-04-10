"""
    Implementación del patrón Template
"""

from abc import ABC, abstractmethod

# Definición de la interfaz Clase que implementa las clases concretas
class Clase(ABC):
    def plantilla(self):
        print("Clase: plantilla")
        self.operacion1()
        self.operacion2()

    @abstractmethod
    def operacion1 (self):
        pass

    @abstractmethod
    def operacion2 (self):
        pass


# Definición de la clase concreta A
class ClaseConcretaA(Clase):
    def operacion1(self):
        print("ClaseConcretaA: operacion1")

    def operacion2(self):
        print("ClaseConcretaA: operacion2")


# Definición de la clase concreta B
class ClaseConcretaB(Clase):
    def operacion1(self):
        print("ClaseConcretaB: operacion1")

    def operacion2(self):
        print("ClaseConcretaB: operacion2")


clase_a = ClaseConcretaA()
clase_b = ClaseConcretaB()
# Llamada a la plantilla
clase_a.plantilla()
clase_b.plantilla()
