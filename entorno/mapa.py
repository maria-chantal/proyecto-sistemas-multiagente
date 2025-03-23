from entorno.celda import Celda
from agentes.semaforo import SemaforoAgent
from agentes.vehiculo import VehiculoAgent
from agentes.paso_peatones import *

class Mapa:
    """Define la cuadrícula donde se moverán los agentes."""
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[Celda("vacio") for _ in range(columnas)] for _ in range(filas)]
        self.entradas = [(0,1),(0,2),(16,32),(16,33), (2,34),(8,0),(14,0)]

    def inicializar_mapa(self):
        """Crea calles e intersecciones en la cuadrícula."""
        for i in range(self.filas):
            self.matriz[i][0] = Celda("plaza")  # Calle vertical sentido 0 = abajo
            self.matriz[i][3] = Celda("plaza")  # Calle vertical sentido 0 = abajo
            self.matriz[i][10] = Celda("plaza")  # Calle vertical sentido 1 = arriba
        for i in range(self.columnas):
            self.matriz[1][i] = Celda("plaza")
            self.matriz[7][i] = Celda("plaza")
            self.matriz[13][i] = Celda("plaza")
        for i in range(self.filas):
            self.matriz[i][1] = Celda("calle", sentido=0)  # Calle vertical sentido 0 = abajo
            self.matriz[i][2] = Celda("calle", sentido=0)  # Calle vertical sentido 0 = abajo
            self.matriz[i][9] = Celda("calle", sentido=1)  # Calle vertical sentido 1 = arriba
            self.matriz[i][25] = Celda("calle", sentido=0)  # Calle vertical sentido 0 = abajo
            self.matriz[i][32] = Celda("calle", sentido=1)  # Calle vertical sentido 1 = arriba
            self.matriz[i][33] = Celda("calle", sentido=1)  # Calle vertical sentido 1 = arriba
        for i in range(self.columnas):
            if self.matriz[2][i].tipo != "vacio" and self.matriz[2][i].tipo != "plaza":
                opciones = [self.matriz[2][i].sentido,3]
                self.matriz[2][i] = Celda("interseccion")  # Calle horizontal sentido 3 izquierda
                self.matriz[2][i].opciones = opciones
            else:
                self.matriz[2][i] = Celda("calle", sentido=3)  # Calle horizontal sentido 3 izquierda

            if self.matriz[8][i].tipo != "vacio" and self.matriz[8][i].tipo != "plaza":
                opciones = [self.matriz[8][i].sentido,2]
                self.matriz[8][i] = Celda("interseccion")  # Calle horizontal sentido 2 derecha
                self.matriz[8][i].opciones = opciones
            else:
                self.matriz[8][i] = Celda("calle", sentido=2)  # Calle horizontal sentido 2 derecha

            if self.matriz[14][i].tipo != "vacio" and self.matriz[14][i].tipo != "plaza":
                opciones = [self.matriz[14][i].sentido,2]
                self.matriz[14][i] = Celda("interseccion")  # Calle horizontal sentido 2 derecha
                self.matriz[14][i].opciones = opciones
            else:
                self.matriz[14][i] = Celda("calle", sentido=2)  # Calle horizontal sentido 2 derecha

        
        ubicacion_semaforos=[(1,1),(1,2),(13,1),(13,2),(14,24),(2,26),(9,32),(9,33)] 
        for i in ubicacion_semaforos:
            self.matriz[i[0]][i[1]].semaforo = SemaforoAgent(i, 5, 5)
        
        ubicacion_pasos=[(2,13),(14,20),(7,1),(7,2),(3,32),(3,33)] 
        for i in ubicacion_pasos:
            self.matriz[i[0]][i[1]].paso = PasoPeatonesAgent(i)

        ubicacion_parking = [(7,17),(7,18)]
        for i in ubicacion_parking:
            self.matriz[i[0]][i[1]] = Celda("parking")

    def obtener_celda(self, x, y):
        """Retorna la celda en una posición específica."""
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            return self.matriz[x][y]
        return None

    def mostrar_mapa(self):
        """Muestra la cuadrícula en la terminal con semáforos actualizados."""
        for i in range(self.filas):
            for j in range(self.columnas):
                celda = self.matriz[i][j]

                if celda is None:
                    print("  ", end=" ")  # Espacio vacío fuera del mapa
                elif celda.tipo == "calle" or celda.tipo == "interseccion":
                    if celda.ocupantes:
                        print(f"🚗{celda.ocupantes[0].id}", end=" ")  # Muestra el ID del vehículo
                    elif hasattr(celda, "semaforo") and celda.semaforo:   
                        estado_semaforo = "🟥 " if celda.semaforo.estado == 0 else "🟩 " # Estado del semáforo
                        print(estado_semaforo, end=" ") 
                    elif hasattr(celda, "paso") and celda.paso:   
                        estado_paso = "🏁 " if celda.paso.estado == 0 else "🚶 " # Estado del paso de peatones
                        print(estado_paso, end=" ")
                    elif celda.tipo == "interseccion":
                        print("🔲 ", end=" ")  # Intersección 
                    else:
                        print("⬜ ", end=" ")  # Calle vacía
                elif celda.tipo == "plaza":
                    if celda.ocupantes:
                        print(f"🚗{celda.ocupantes[0].id}", end=" ")  # Muestra el ID del vehículo
                    else:
                        print("​🟦 ", end=" ")  # Plaza vacia
                elif celda.tipo == "parking":
                    print("🔼 ", end=" ")  # Plaza vacia
                else:
                    print("⬛ ", end=" ")  # Resto del mapa
            print()  # Nueva línea
        




