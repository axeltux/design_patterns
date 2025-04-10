"""
    Implementación del patrón Visitor
"""

# Definición de la interfaz Elemento
class Elemento:
    def aceptar(self, visitante):
        pass


# Definición de la clase ElementoConcretoA
class ElementoConcretoA(Elemento):
    def aceptar(self, visitante):
        visitante.visitar_elemento_a(self)
        print("ElementoConcretoA: aceptando al visitante.")

# Definición de la clase ElementoConcretoB
class ElementoConcretoB(Elemento):
    def aceptar(self, visitante):
        visitante.visitar_elemento_b(self)
        print("ElementoConcretoB: aceptando al visitante.")


# Definición de la interfaz Visitante
class Visitante:
    def visitar_elemento_a(self, elemento):
        pass

    def visitar_elemento_b(self, elemento):
        pass


# Definición de la clase concreta VisitanteConcreto1
class VisitanteConcreto1(Visitante):
    def visitar_elemento_a(self, elemento):
        print("VisitanteConcreto1: visitando ElementoConcretoA")

    def visitar_elemento_b(self, elemento):
        print("VisitanteConcreto1: visitando ElementoConcretoB")


# Definición de la clase concreta VisitanteConcreto2
class VisitanteConcreto2(Visitante):
    def visitar_elemento_a(self, elemento):
        print("VisitanteConcreto2: visitando ElementoConcretoA")

    def visitar_elemento_b(self, elemento):
        print("VisitanteConcreto2: visitando ElementoConcretoB")


# Creación de los objetos necesarios
elementos = [ElementoConcretoA(), ElementoConcretoB(), ElementoConcretoA()]
visitor1 = VisitanteConcreto1()
visitor2 = VisitanteConcreto2()

# Iterar sobre los elementos y aceptar el visitante
for elemento in elementos:
    elemento.aceptar(visitor1)

for elemento in elementos:
    elemento.aceptar(visitor2)
