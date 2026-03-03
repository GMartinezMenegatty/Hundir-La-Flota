class Nave:
    def __init__(self, nombre: str, tamano: int):
        self.nombre = nombre
        self.tamano = tamano
        self.vida = tamano

    def recibir_disparo(self) -> str:
        if self.vida > 0:
            self.vida -= 1

        if self.vida == 0:
            return "Hundido"
        else:
            return "Tocado"