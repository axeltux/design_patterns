"""
    Implementación del patrón Memento 
    El patrón Memento permite capturar y almacenar el estado interno de un objeto sin violar
    su encapsulamiento, de modo que el objeto pueda ser restaurado a este estado más tarde.
"""

# Definición de la clase Memento
class Memento:
    def __init__(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado

# Definición de la clase Origen
class Origen:
    def __init__(self, estado):
        self._estado = estado

    def set_estado(self, estado):
        print(f"Originador: estableciendo estado a {estado}")
        self._estado = estado

    def get_estado(self):
        return self._estado

    def crear_memento(self):
        print(f"Originador: creando memento")
        return Memento(self._estado)

    def establecer_memento(self, memento):
        estado = memento.get_estado()
        print(f"Originador: estado despues de restaurar Memento: {estado}")
        self._estado = estado


# Definición de la clase Cuidador
class Cuidador:
    def __init__(self, originador):
        self._mementos = []
        self._originador = originador

    def backup(self):
        print("Cuidador: guardando el estado memento")
        self._mementos.append(self._originador.crear_memento())

    def deshacer(self):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        print(f"Cuidador: restaurando el estado a {memento.get_estado()}")
        try:
            self._originador.establecer_memento(memento)
        except Exception as e:
            self.deshacer()


originador = Origen("1-2-3-4-5.")
cuidadora = Cuidador(originador)
cuidadora.backup()
originador.set_estado("1-2-3-4.")
cuidadora.backup()
originador.set_estado(f"1-2-3.")
cuidadora.backup()
originador.set_estado("1-2.")
print("Estado actual:", originador.get_estado())
cuidadora.deshacer()
cuidadora.deshacer()
cuidadora.deshacer()
