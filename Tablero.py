from Nave import Nave


class Tablero:

    def __init__(self, tamano=10):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        self.casillero = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, por1, por1, por1, por1, por1, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, sub1, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra2, fra2, fra2, None, None, sub3, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra3, fra3, fra3, None, sub4, None, None, None, sub2]
        ]

    def colocar_nave(self, nave, x, y, orientacion):
        if orientacion == "H":
            for i in range(nave.vida):
                self.casillero[x][y + i] = nave

        elif orientacion == "V":
            for i in range(nave.vida):
                self.casillero[x + i][y] = nave

    def comprobar_impacto(self, x, y):

        print(f"[LOG] estoy en tablero comprobando impacto ({x}, {y})")
        print(f"[LOG] casillero[{x}][{y}] = {self.casillero[x][y]}")

        if self.casillero[x][y] is None:
            print("[LOG] Agua")
            return self.AGUA

        nave = self.casillero[x][y]

        resultado = nave.recibir_disparo()

        if resultado == 1:
            print(f"[LOG] {nave.nombre} Tocado")
            return self.TOCADO

        elif resultado == 2:
            print(f"[LOG] {nave.nombre} Hundido")
            return self.HUNDIDO
        return None