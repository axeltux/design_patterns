"""
    Implementación del patrón Bridge
"""
from abc import ABC, abstractmethod

class Interfaz(ABC):
    @abstractmethod
    def metodo(self):
        pass


class ImplementacionConcreta1(Interfaz):
    def metodo(self):
        print(f"Implementación concreta 1")


class ImplementacionConcreta2(Interfaz):
    def metodo(self):
        print(f"Implementación concreta 2")


class Abstaccion:
    def __init__(self, interfaz):
        self._interfaz = interfaz

    def funcionalidad1(self):
        self._interfaz.metodo()


abstaccion1 = Abstaccion(ImplementacionConcreta1())
abstaccion1.funcionalidad1()
abstaccion2 = Abstaccion(ImplementacionConcreta2())
abstaccion2.funcionalidad1()

