"""
    Implementación del patrón Mediator
"""

# Definición de la interfaz Mediador
class Mediador:
    def enviar_mensaje(self, componente, mensaje):
        pass


# Definición de la clase Mediador Concreto
class MediadorConcreto(Mediador):
    def __init__(self, componenteA, componenteB):
        self._componenteA = componenteA
        self._componenteB = componenteB

    def enviar_mensaje(self, componente, mensaje):
        if isinstance(componente, ComponenteA):
            self._componenteB.recibir_mensaje(mensaje)
        else:
            self._componenteA.recibir_mensaje(mensaje)


# Definición de la interfaz Componente
class Componente:
    def __init__(self, mediador):
        self._mediador = mediador

    def enviar_mensaje(self, mensaje):
        self._mediador.enviar_mensaje(self, mensaje)

    def recibir_mensaje(self, mensaje):
        pass


# Definición de la clase Componente A
class ComponenteA(Componente):
    def recibir_mensaje(self, mensaje):
        print("Componente A mensaje recibido: {}".format(mensaje))


# Definición de la clase Componente B
class componenteB(Componente):
    def recibir_mensaje(self, mensaje):
        print("Componente B mensaje recibido: {}".format(mensaje))


# Creación de los objetos necesarios
mediador = MediadorConcreto(ComponenteA(Mediador), componenteB(Mediador))
componente_a = ComponenteA(mediador)
componente_b = componenteB(mediador)

# Enviar un mensaje desde componente_a a componente_b desde el mediador
componente_a.enviar_mensaje("Hola desde el componente A!")
componente_b.enviar_mensaje("Hola desde el componente B!")


