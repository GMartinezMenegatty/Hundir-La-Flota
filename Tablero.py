from Nave import Nave
from casilla import Casilla
class Tablero:

    def __init__(self, tamano = 10):
        self.tamano = tamano

        self.AGUA = 0 #Inicializamos agua para que tenga el valor de 0
        self.TOCADO = 1 #Inicializamos tocado para que tenga el valor de 1
        self.HUNDIDO = 2 #Inicializamos hundido para que tenga el valor de 2

        por1 = Nave("Enterprise", "portaaviones", 5) #los nombres, tipos y vida de las naves

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)



        self.casillero = [ #Creamos el tablero
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()]
        ]

        # portaaviones
        self.casillero[1][1].nave = por1 #Los portaaviones estaran en esas posiciones
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1
        self.casillero[1][4].nave = por1
        self.casillero[1][5].nave = por1

        # fragatas
        self.casillero[3][3].nave = fra1 #Las fragatas estaran en esas posiciones
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1

        self.casillero[7][1].nave = fra2
        self.casillero[7][2].nave = fra2
        self.casillero[7][3].nave = fra2

        self.casillero[9][1].nave = fra3
        self.casillero[9][2].nave = fra3
        self.casillero[9][3].nave = fra3

        # submarinos
        self.casillero[4][6].nave = sub1 #Los submarinos estaran en esas posiciones
        self.casillero[9][9].nave = sub2
        self.casillero[7][6].nave = sub3
        self.casillero[9][5].nave = sub4

    def comprobar_impacto(self, x, y):
        print(f"[LOG] comprobando impacto ({x}, {y})") #Se muestra el impacto a las coordenadas

        casilla = self.casillero[x][y]
        resultado = casilla.disparar() #Se dispara a la casilla

        if resultado is None:
            return self.AGUA  #Si la casilla no tiene nada sera agua

        return resultado #Se devuelve el resultado