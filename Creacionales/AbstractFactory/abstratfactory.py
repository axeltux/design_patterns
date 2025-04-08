"""
    Implementación del patrón Abstract Factory
"""

# Definición de la clase abstracta AbstractFactory
class AbstractFactory:
    def crear_producto_a(self):
        pass

    def crear_producto_b(self):
        pass


# Definición de la clase concreta Factory1 que implementa la clase AbstractFactory
class Factory1(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA1()

    def crear_producto_b(self):
        return ProductoB1()


# Definición de la clase concreta Factory2 que implementa la clase AbstractFactory
class Factory2(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA2()

    def crear_producto_b(self):
        return ProductoB2()


# Definición de la clase abstracta ProductoA
class ProductoA:
    def descripcion(self):
        pass


# Definición de la clase concreta ProductoA1
class ProductoA1(ProductoA):
    def descripcion(self):
        return f"Soy un producto de tipo A1"


# Definición de la clase concreta ProductoA2
class ProductoA2(ProductoA):
    def descripcion(self):
        return f"Soy un producto de tipo A2"


# Definición de la clase abstracta ProductoB
class ProductoB:
    def descripcion(self):
        pass


# Definición de la clase concreta ProductoB1
class ProductoB1(ProductoB):
    def descripcion(self):
        return f"Soy un producto de tipo B1"


# Definición de la clase concreta ProductoB2
class ProductoB2(ProductoB):
    def descripcion(self):
        return f"Soy un producto de tipo B2"


# Ejemplo de implementación del patrón Abstract Factory
if __name__ == '__main__':
    factory_1 = Factory1()
    producto_a1 = factory_1.crear_producto_a()
    producto_b1 = factory_1.crear_producto_b()
    print(producto_a1.descripcion())
    print(producto_b1.descripcion())

    factory_2 = Factory2()
    producto_a2 = factory_2.crear_producto_a()
    producto_b2 = factory_2.crear_producto_b()
    print(producto_a2.descripcion())
    print(producto_b2.descripcion())

