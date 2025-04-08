"""
  Implementación del patrón Singleton
"""

class Singleton:
  __instance = None

  """
    Método estático que permite el acceso a la instancia 
    única de la clase
  """
  @staticmethod
  def getInstance():
    if Singleton.__instance == None:
      Singleton()
    return Singleton.__instance

  """
    El constructor es privado para asegurarse que solo 
    se puede crear una instancia
  """
  def __init__(self):
    if Singleton.__instance != None:
      raise Exception("Esta clase es un Singleton, no se pueden crear mas de una instancia")
    else:
      Singleton.__instance = self


# Crear las instancias de la clase Singleton
singleton1 = Singleton.getInstance()
singleton2 = Singleton.getInstance()

# Conprobar si ambas instancias son las mismas
print(singleton1 is singleton2)

