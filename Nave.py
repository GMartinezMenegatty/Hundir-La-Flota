
class Nave:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir_disparo(self):
        if self.vida > 0:
            self.vida -= 1

        if self.vida <= 0:
            return 2
        else:
            return 1

    def __str__ (self):
        return f"{self.vida}, {self.nombre}, {self.tipo}"
