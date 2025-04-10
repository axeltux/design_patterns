"""
    Implementación del patrón State
"""

# Definición de la clase Contexto
class Contexto:
    def __init__(self):
        self._estado = None

    def establecer_estado(self, estado):
        print(f"Contexto: estableciendo nuevo estado {estado}")
        self._estado = estado

    def peticion(self):
        self._estado.manejar()


# Definición de la interfaz Estado
class Estado:
    def manejar(self):
        pass


# Definición de la clase EstadoConcretoA
class EstadoConcretoA(Estado):
    def manejar(self):
        print("EstadoConcretoA: manejando la solicitud.")

# Definición de la clase EstadoConcretoB
class EstadoConcretoB(Estado):
    def manejar(self):
        print("EstadoConcretoB: manejando la solicitud.")


# Creación de los objetos necesarios
contexto = Contexto()
estado_a = EstadoConcretoA()
estado_b = EstadoConcretoB()
# Establecer el estado del contexto
contexto.establecer_estado(estado_a)
# Realizar una petición
contexto.peticion()
# Cambiar el estado del contexto
contexto.establecer_estado(estado_b)
# Realizar otra petición
contexto.peticion()
