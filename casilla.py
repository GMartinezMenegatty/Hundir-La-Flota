class Casilla:
    def __init__(self):
        self.nave = None #Se inicializan las naves y por defecto no hay
        self.atacada = False #Por defecto no esta atacada, es decir, visitada la casilla

    def disparar(self):
        if self.atacada: # Si la casilla esta atacada, imprime por pantalla que ya se disparo
            print("[LOG] Ya disparaste aquí")
            return None #Si no, no devuelve nada

        self.atacada = True # Se cambia el valor de la variable, ya que ya se disparo una vez

        if self.nave is None: #Si no hay nave, devuelve agua
            print("[LOG] Agua")
            return 0

        resultado = self.nave.recibir_disparo() # Se almacena el disparo

        if resultado == 2: #Si el resultado es 2, esta hundida la nave
            print(f"[LOG] {self.nave.nombre} Hundido")
        else: #Si no, estara tocada la nave
            print(f"[LOG] {self.nave.nombre} Tocado ({self.nave.vida} vida restante)")

        return resultado #Se devuelve el resultado