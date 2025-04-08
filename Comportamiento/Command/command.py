"""
    Implementación de patrón Command
"""

# Definición de la clase Receptor que va a recibir y ejecutar las acciones
class Receptor:
    def ejecutar(self):
        print(f"Ejecutando la acción del receptor")


# Definición de la clase Comando que es la interfaz común
class Comando:
    def ejecutar(self):
        pass


# Defeinicion de la clase ComandoConcreto
class ComandoConcreto(Comando):
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        self.receptor.ejecutar()


# Definición de la clase Invocador
class Invocador:
    def establecer_comando(self, comando):
        self.comando = comando

    def ejecutar_comando(self):
        self.comando.ejecutar()


# Crear las instancias de las clases
receptor = Receptor()
comando_concreto = ComandoConcreto(receptor)
invocador = Invocador()

# Asignar ComandoConcreto al Invocador
invocador.establecer_comando(comando_concreto)

# Ejecutar acción a traves del Invocador
invocador.ejecutar_comando()


