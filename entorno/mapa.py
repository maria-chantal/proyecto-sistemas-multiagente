from entorno.celda import Celda
from agentes.semaforo import SemaforoAgent
from agentes.vehiculo import VehiculoAgent

class Mapa:
    """Define la cuadrícula donde se moverán los agentes."""
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[Celda("vacio") for _ in range(columnas)] for _ in range(filas)]

    def inicializar_mapa(self):
        """Crea calles e intersecciones en la cuadrícula."""
        for i in range(self.filas):
            self.matriz[i][3] = Celda("calle", carriles=1)  # Calle vertical
        for i in range(self.columnas):
            self.matriz[5][i] = Celda("calle", carriles=2)  # Calle horizontal

        # ✅ Asegurar que la celda (5,3) tenga un semáforo
        if isinstance(self.matriz[5][3], Celda):  # Solo si ya es una calle
            self.matriz[5][3].semaforo = SemaforoAgent((5, 3), 5, 5)  
 






    def obtener_celda(self, x, y):
        """Retorna la celda en una posición específica."""
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            return self.matriz[x][y]
        return None

    def mostrar_mapa(self):
        """Muestra la cuadrícula en la terminal con semáforos actualizados."""
        for i in range(self.filas):
            for j in range(self.columnas):
                celda = self.obtener_celda(i, j)

                if celda is None:
                    print("  ", end=" ")  # Espacio vacío fuera del mapa
                elif celda.tipo == "calle":
                    if celda.ocupantes:
                        print(f"🚗{celda.ocupantes[0].id}", end=" ")  # Muestra el ID del vehículo
                    elif hasattr(celda, "semaforo") and celda.semaforo:  # ✅ Verifica si hay semáforo
                        estado_semaforo = "🟥" if celda.semaforo.estado == "rojo" else "🟩"
                        print(estado_semaforo, end=" ")  
                    else:
                        print("⬜", end=" ")  # Calle vacía
                elif celda.tipo == "intersección":
                    print("🔲", end=" ")  # Intersección
                else:
                    print("⬛", end=" ")  # Otros elementos
            print()  # Nueva línea





