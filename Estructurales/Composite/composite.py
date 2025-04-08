"""
    Implementación del patrón Composite
"""
from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def operacion(self):
        pass


class Hoja(Componente):
    def __init__(self, numero):
        self._numero = numero

    def operacion(self):
        print(f"Realizando operaciones en Hoja {self._numero}")


class Compuesto(Componente):
    def __init__(self, numero):
        self._elementos = []
        self._numero = numero

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)

    def quitar_elemento(self, elemento):
        self._elementos.remove(elemento)

    def operacion(self):
        print(f"Realizando operación de composición {self._numero}")
        for elemento in self._elementos:
            elemento.operacion()


hoja1 = Hoja(1)
hoja2 = Hoja(2)

comp1 = Compuesto(1)
comp1.agregar_elemento(hoja1)
comp1.agregar_elemento(hoja2)

hoja3 = Hoja(3)

comp2 = Compuesto(2)
comp2.agregar_elemento(comp1)
comp2.agregar_elemento(hoja3)

comp2.operacion()

