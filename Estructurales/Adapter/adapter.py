"""
    Implementación del patrón Adapter
"""
from abc import ABC, abstractmethod

class Interfaz(ABC):
    @abstractmethod
    def metodo1(self):
        pass

    @abstractmethod
    def metodo2(self):
        pass


class Servicio:
    def metodo1(self):
        return "metodo1"


class AdaptadorServicio(Interfaz):
    def __init__(self, servicio):
        self.servicio = servicio

    def metodo1(self):
        return self.servicio.metodo1()

    def metodo2(self):
        return "metodo2 (adaptado)"


servicio = Servicio()
adaptador = AdaptadorServicio(servicio)

print(f"El servicio tiene {adaptador.metodo1()} y {adaptador.metodo2()}")

