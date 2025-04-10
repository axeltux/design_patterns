"""
    Implementación del patron Strategy
"""

from abc import ABC, abstractmethod

# Definición de la clase abstracta Estrategia
class Estrategia(ABC):
    @abstractmethod
    def ejecutar(self):
        pass


# Definición de la clase EstrategiaConcretaA
class EstrategiaConcretaA(Estrategia):
    def ejecutar(self):
        print("Estrategia Concreta A: Ejecutando estrategia A.")


# Definición de la clase EstrategiaConcretaB
class EstrategiaConcretaB(Estrategia):
    def ejecutar(self):
        print("Estrategia Concreta B: Ejecutando estrategia B.")


# Definición de la clase Contexto
class Contexto:
    def __init__(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def establecer_estrategia(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def ejecutar_estrategia(self):
        print("Contexto: Ejecutando estrategia.")
        self._estrategia.ejecutar()


# Creación de los objetos necesarios
conteto = Contexto(EstrategiaConcretaA())
# Ejecutar la estrategia inicial
conteto.ejecutar_estrategia()
# Cambiar la estrategia
conteto.establecer_estrategia(EstrategiaConcretaB())
# Ejecutar la nueva estrategia
conteto.ejecutar_estrategia()
# Cambiar la estrategia
conteto.establecer_estrategia(EstrategiaConcretaA())
# Ejecutar la nueva estrategia
conteto.ejecutar_estrategia()

