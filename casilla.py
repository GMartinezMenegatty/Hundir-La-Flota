class Casilla:
    def __init__(self):
        self.nave = None
        self.atacada = False

    def disparar(self):
        if self.atacada:
            print("[LOG] Ya disparaste aquí")
            return None

        self.atacada = True

        if self.nave is None:
            print("[LOG] Agua")
            return 0

        resultado = self.nave.recibir_disparo()

        if resultado == 2:
            print(f"[LOG] {self.nave.nombre} Hundido")
        else:
            print(f"[LOG] {self.nave.nombre} Tocado ({self.nave.vida} vida restante)")

        return resultado