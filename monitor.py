

from Computadora import *

class Alumno (Computadora):

    def __init__(self,tipo,modelo):
        self.tipo=tipo
        self.modelo=modelo

    def encender(self):
        super().encender()

    def apagar(self):
        super().apagar()

    def suspender(self):
        return f"esta {self.tipo} y suspeder"

    def conectar(self):
        super().conectar()

    def desconectar(self):
        super().desconectar()