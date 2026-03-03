from Nave import Nave

class Tablero:
    def __init__(self, tamano: int = 10):
        self.tamano = tamano
        # Matriz inicializada en None (sin nave)
        self.matriz = [[None for _ in range(tamano)] for _ in range(tamano)]

    def colocar_nave(self, nave: Nave, x: int, y: int, orientacion: str):
        if orientacion == "H":  # Horizontal
            for i in range(nave.tamano):
                self.matriz[x][y + i] = nave
        elif orientacion == "V":  # Vertical
            for i in range(nave.tamano):
                self.matriz[x + i][y] = nave

    def comprobar_impacto(self, x: int, y: int) -> tuple:
        nave = self.matriz[x][y]

        if nave is None:
            return ("Agua", None)

        resultado = nave.recibir_disparo()
        return (resultado, nave)