from entorno.celda import Celda
from agentes.semaforo import SemaforoAgent
from agentes.vehiculo import VehiculoAgent

class Mapa:
    """Define la cuadrícula donde se moverán los agentes."""
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[None for _ in range(columnas)] for _ in range(filas)]

    def inicializar_mapa(self):
        """Crea calles y semáforos en la cuadrícula."""
        for i in range(1, self.filas-1):
            self.matriz[i][3] = Celda("calle", carriles=1)
            self.matriz[5][i] = Celda("calle", carriles=2)

        # Agregar semáforos
        self.matriz[5][3] = Celda("semaforo")
        self.matriz[5][3].semaforo = SemaforoAgent((5, 3), 5, 5)

    def obtener_celda(self, x, y):
        """Retorna la celda en una posición específica."""
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            return self.matriz[x][y]
        return None

vehiculos = [VehiculoAgent(id=i, ubicacion=(0, 3), destino=(9, 3)) for i in range(3)]

