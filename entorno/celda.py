class Celda:
    def __init__(self, tipo, sentido=0):
        self.tipo = tipo  # "calle", "intersección"
        self.sentido = sentido
        self.ocupantes = []  # Lista de vehículos en la celda
        self.semaforo = None 
        self.paso = None
        self.opciones=[] # Opciones de los coches para girar
