class Celda:
    def __init__(self, tipo, carriles=1):
        self.tipo = tipo  # "calle", "intersección"
        self.carriles = carriles
        self.ocupantes = []  # Lista de vehículos en la celda
