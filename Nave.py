
class Nave:
    def __init__(self, nombre, tipos, vidas):
        self.nombre = nombre
        self.tipo = tipos
        self.vida = vidas

    def recibir_disparo(self):
        self.vida -= 1

        if self.vida <= 0:
            return 2
        else:
            return 1

    def __str__ (self):
        return f"{self.vida}, {self.nombre}, {self.tipo}"
