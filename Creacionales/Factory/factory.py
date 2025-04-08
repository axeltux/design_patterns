"""
    Implementación del patrón Factory
"""

# Definición de la clase abstracta Producto
class Producto:
    def descripcion(self):
        pass


# Definición de la clase concreta ProductoA que implementa la interfaz Producto
class ProductoA(Producto):
    def descripcion(self):
        return "Soy un producto de tipo A"


# Definición de la clase concreta ProductoB que implementa la interfaz Producto
class ProductoB(Producto):
    def descripcion(self):
        return "Soy un producto de tipo B"


# Definición de la clase abstracta Creador
class Creador():
    def crear_producto(self):
        pass


# Definición de la clase concreta CreadorA que implementa la clase abstracta Creador
class CreadorA(Creador):
    def crear_producto(self):
        return ProductoA()


# Definición de la clase concreta CreadorB que implementa la clase abstracta Creador
class CreadorB(Creador):
    def crear_producto(self):
        return ProductoB()


# Ejemplo del uso del patrón Factory Method
if __name__ == '__main__':
    creador_a = CreadorA()
    producto_a = creador_a.crear_producto()
    print(producto_a.descripcion())

    creador_b = CreadorB()
    producto_b = creador_b.crear_producto()
    print(producto_b.descripcion())


