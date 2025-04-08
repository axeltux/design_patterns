"""
    Implementación del patrón Chain of Responsability
"""

# Definición de la clase manejadora base
class Manejador:
    def __init__(self, sucesor = None):
        self._sucesor = sucesor

    def manejar_peticion(self, peticion):
        manejada = self._manejar(peticion)
        if not manejada:
            self._sucesor.manejar_peticion(peticion)

    def _manejar(self, peticion):
        raise NotImplementedError(f"La implementación debe hacerse en una subclase")


# Definición de la clase Manejador Concreto A
class ManejadorConcretoA(Manejador):
    def _manejar(self, peticion):
        if 0 < peticion <= 10:
            print(f"Petición {peticion} gestionada por ManejadorConcretoA")
            return True
        else:
            return False


# Definición de la clase Manejador Concreto B
class ManejadorConcretoB(Manejador):
    def _manejar(self, peticion):
        if 10 < peticion <= 20:
            print(f"Petición {peticion} gestionada por ManejadorConcretoB")
            return True
        else:
            return False


# Definición de la clase Manejador Concreto C
class ManejadorConcretoC(Manejador):
    def _manejar(self, peticion):
        if 20 < peticion <= 30:
            print(f"Petición {peticion} gestionada por ManejadorConcretoC")
            return True
        else:
            return False


# Definición de la clase manejador por defecto
class ManejadorPorDefecto(Manejador):
    def _manejar(self, peticion):
        print(f"No hay manejador definido para la petición {peticion}")
        return True


# Configurar cadena de responsabilidad
manejador_a = ManejadorConcretoA()
manejador_b = ManejadorConcretoB()
manejador_c = ManejadorConcretoC()
manejador_defecto = ManejadorPorDefecto()

manejador_a._sucesor = manejador_b
manejador_b._sucesor = manejador_c
manejador_c._sucesor = manejador_defecto

for peticion in [15, 45, 500, 75]:
    manejador_a.manejar_peticion(peticion)


