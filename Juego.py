from Tablero import Tablero
#Clase Principal que Almacena el juego

class Juego:

    def __init__(self):
        self.obj_tablero = Tablero() #Creamos el tablero del juego
        self.atacado = [] #Creamos el ataque

    def lanzar_ataque(self, x, y):
        print(f"Atacando a  {x}, {y} ") #Se ataca a las coordenadas
        atack = (x ,y) #Se almacenan las coordenadas
        if atack not in self.atacado: #Si las coordenadas no estan en el ataque
            resultado = self.obj_tablero.comprobar_impacto(x, y) #Resultado almacenara el impacto a las coordenadas
            self.mostrar_resultado(resultado)
            self.atacado.append(atack) #Se añaden las coordenadas a ataque
        else:
            print(f"[LOG] Ya atacaste esta casilla") #Si ya se ataco, se muestra

    def mostrar_resultado(self, resultado):
        if resultado == 0: #Si el resultado al ataque de la coordenada es 0, sera Agua
            print("Agua")
        elif resultado == 1: #Si el resultado al ataque de la coordenada es 1, sera Tocada (la nave)
            print("Tocado")
        elif resultado == 2: #Si el resultado al ataque de la coordenada es 2, estara hundida la nave
            print("Hundido")

if __name__ == "__main__":
    juego = Juego()
    juego.lanzar_ataque(2, 3) #Lanzamos los ataques
    print()
    juego.lanzar_ataque(2, 3) #Lanzamos los ataques
    print()
    juego.lanzar_ataque(1, 1) #Lanzamos los ataques
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