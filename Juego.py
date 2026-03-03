from Nave import Nave
from Tablero import Tablero, Estado


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.inicializar_naves()

    def inicializar_naves(self):
        submarino = Nave("Submarino", 1)
        buque = Nave("Buque", 2)
        portaaviones = Nave("Portaaviones", 4)

        self.tablero.colocar_nave(submarino, 0, 0, "H")
        self.tablero.colocar_nave(buque, 2, 2, "H")
        self.tablero.colocar_nave(portaaviones, 5, 3, "V")

    def lanzar_ataque(self, x: int, y: int):
        resultado, nave = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado, nave)

    def mostrar_resultado(self, resultado:str, nave):
        if resultado == "Agua":
            return Estado.agua
        elif resultado == "Tocado":
            return Estado.tocado
        elif resultado == "Hundido":
            return Estado.hundido


if __name__ == "__main__":
    juego = Juego()

    while True:
        try:
            x = int(input("Introduce fila (0-9): "))
            y = int(input("Introduce columna (0-9): "))
            juego.lanzar_ataque(x, y)
        except:
            print("Entrada inválida.")