# Clase principal que gestiona el juego
from Tablero import Tablero


class Juego:
    def __init__(self):
        self.lanzar_ataque(9, 1)
        self.lanzar_ataque(4, 0)
        self.lanzar_ataque(7, 6)

    def inicializar_naves(self):
        self.tablero = Tablero()

    def mostrar_resultado(self, resultado: int):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):

        print(f"Atacando a  {x}, {y} ")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
    Juego()