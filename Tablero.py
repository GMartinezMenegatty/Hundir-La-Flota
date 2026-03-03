from Nave import Nave

class Estado:
    agua = 0
    tocado = 1
    hundido = 2

class Tablero:
    def __init__(self, tamano: int = 10):
        self.tamano = tamano
        self.matriz = [[None for _ in range(tamano)] for _ in range(tamano)]

    def colocar_nave(self, nave: Nave, x: int, y: int, orientacion: str):
        if orientacion == "H":
            for i in range(nave.tamano):
                self.matriz[x][y + i] = nave
        elif orientacion == "V":
            for i in range(nave.tamano):
                self.matriz[x + i][y] = nave

    def comprobar_impacto(self, x: int, y: int) -> tuple:
        nave = self.matriz[x][y]

        if nave is None:
            return (self.agua, None)

        resultado = nave.recibir_disparo()
        return (resultado, nave)