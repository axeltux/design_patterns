"""
    Implementación del patrón Iterator
"""

# Definición de la clase iterador concreto
class MiIterador:
    def __init__(self, dato):
        self.index = 0
        self.dato = dato

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dato):
            raise StopIteration
        result = self.dato[self.index]
        self.index += 1
        return result


# Definición de la clase colección concreta
class MiColeccion:
    def __init__(self):
        self.dato = []

    def add_item(self, item):
        self.dato.append(item)

    def __iter__(self):
        return MiIterador(self.dato)


coleccion = MiColeccion()
coleccion.add_item("Elemento 1")
coleccion.add_item("Elemento 2")
coleccion.add_item("Elemento 3")

for item in coleccion:
    print(item)


