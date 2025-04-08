"""
    Implementación del patrón Proxy
"""

# Definición de la interfaz de servicio
class InterfazServicio:
    def realizar_accion(self):
        pass


class Servicio(InterfazServicio):
    def realizar_accion(self):
        print(f"Realizando acción")


class Proxy(InterfazServicio):
    def __init__(self):
        self.servicio = None

    def realizar_accion(self):
        if self.servicio is None:
            self.servicio = Servicio()
        self.servicio.realizar_accion()


# Ejemplo de uso
proxy = Proxy()
proxy.realizar_accion()

