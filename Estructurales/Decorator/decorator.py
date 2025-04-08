"""
    Implementación del patrón Decorator
"""
from abc import ABC, abstractmethod

class Componente(ABC):
    def operacion(self):
        pass


# Definición de la clase concreta que implementa la clase base base
class ComponenteConcreto(Componente):
    def operacion(self):
        print(f"Realizando operación de componente concreto")


# Definición de la clase decoradora base que tambien implementa la clase base
class Decorador(Componente):
    def __init__(self, componente):
        self._componente = componente

    def operacion(self):
        self._componente.operacion()


# Definición de la clase decoradora que agrega funcionalidad al componente base
class DecoradorConcreto(Decorador):
    def __init__(self, componente):
        super().__init__(componente)

    def operacion(self):
        super().operacion()
        self.agregar_funcionalidad()

    def agregar_funcionalidad(self):
        print(f"Agregando funcionalidad al componente")


componente = ComponenteConcreto()
decorador = DecoradorConcreto(componente)
decorador.operacion()

