from Tablero import Tablero


class Juego:

    def __init__(self):
        self.obj_tablero = Tablero()
        self.atacado = []

    def lanzar_ataque(self, x, y):
        print(f"Atacando a  {x}, {y} ")
        atack = (x ,y)
        if atack not in self.atacado:
            resultado = self.obj_tablero.comprobar_impacto(x, y)
            self.mostrar_resultado(resultado)
            self.atacado.append(atack)
        else:
            print(f"[LOG] Ya atacaste esta casilla")

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Awa")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

if __name__ == "__main__":
    juego = Juego()
    juego.lanzar_ataque(2, 3)
    print()
    juego.lanzar_ataque(2, 3)
    print()
    juego.lanzar_ataque(1, 1)
    print()
    juego.lanzar_ataque(1, 2)
    print()
    juego.lanzar_ataque(1, 3)
    print()
    juego.lanzar_ataque(1, 4)
    print()
    juego.lanzar_ataque(1, 4)
    print()
    juego.lanzar_ataque(1, 5)
    print()
    juego.lanzar_ataque(0, 4)
    print()
    juego.lanzar_ataque(7, 6)