#Clase que almacena la nave

class Nave:

    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre #Inicializamos el nombre de la nave
        self.tipo = tipo #Inicializamos el tipo de la nave
        self.vida = vida #Inicializamos la Vida de la nave

    def recibir_disparo(self):
        self.vida -= 1 #La vida se ira restando

        if self.vida > 0: #Si la vida es mayor que 0
            return 1 # Se toca una nave
        else:
            return 2 # Si es menor que 0 estara Hundida

    def __str__(self):
        return f"{self.nombre} {self.tipo} {self.vida}" #Mostramos el resultado