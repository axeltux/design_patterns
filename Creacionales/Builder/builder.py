"""
    Implementación del patrón Builder
"""

# Definición de la clase Pizza y sus atributos
class Pizza:
    def __init__(self):
        self.size = ""
        self.chesee = False
        self.pepperoni = False
        self.ham = False
        self.mushrooms = False
        self.tomatoes = False
        self.masa_type = ""


"""
    Definición de la clase Builder, define los métodos para 
    construir los objetos de Pizza
"""
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def add_chesee(self):
        self.pizza.chesee = True

    def add_pepperoni(self):
        self.pizza.pepperoni = True

    def add_ham(self):
        self.pizza.ham = True

    def add_mushrooms(self):
        self.pizza.mushrooms = True

    def add_tomatoes(self):
        self.pizza.tomatoes = True

    def set_masa_type(self, masa_type):
        self.pizza.masa_type = masa_type

    def get_result(self):
        return self.pizza


"""
    Definición de un Director que utilizara Builder para construir
    diferentes tipos de pizza
"""
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_margarita(self):
        self._builder.set_size("12 inches")
        self._builder.add_chesee()
        self._builder.add_tomatoes()
        self._builder.set_masa_type("thin crush")

    def construct_pepperoni(self):
        self._builder.set_size("16 inches")
        self._builder.add_chesee()
        self._builder.add_pepperoni()
        self._builder.add_mushrooms()
        self._builder.set_masa_type("thick crust")


# Construcción de las Pizzas usando Builder
pizza_builder = PizzaBuilder()
director = Director(pizza_builder)

director.construct_margarita()
pizza = pizza_builder.get_result()
print(pizza.__dict__)

director.construct_pepperoni()
pizza = pizza_builder.get_result()
print(pizza.__dict__)


