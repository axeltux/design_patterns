"""
    Implementación del patrón Flyweight
"""

# Definición de la clase Flyweight
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight con estado compartido '{self.shared_state}' y estado único '{unique_state}'.")


# Definición d ela factoria Flyweight
class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]


factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("Estado compartido")
flyweight1.operation("Estado único 1")

flyweight2 = factory.get_flyweight("Estado compartido")
flyweight2.operation("Estado único 2")

flyweight3 = factory.get_flyweight("Estado compartido 2")
flyweight3.operation("Estado único 3")

