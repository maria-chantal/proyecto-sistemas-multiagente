from time import sleep
from entorno.mapa import Mapa
from agentes.vehiculo import VehiculoAgent
from agentes.semaforo import SemaforoAgent
import sys

# Clase para guardar un txt con los logs
class Logger:
    def __init__(self, archivo_log):
        self.terminal = sys.stdout
        self.log = open(archivo_log, "w", encoding="utf-8")

    def write(self, mensaje):
        self.terminal.write(mensaje)
        self.log.write(mensaje)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger("logs_simulacion.txt")

class Simulacion:
    def __init__(self, filas, columnas, num_vehiculos):
        self.mapa = Mapa(filas, columnas)
        self.mapa.inicializar_mapa()
        self.num_vehiculos_gen = num_vehiculos
        self.tiempos_parados = []

        # Crear lista de vehículos
        self.vehiculos = []
        for i in range(num_vehiculos):
            # Asegurarse de que la posición inicial es una calle
            vehiculo = VehiculoAgent(id=i+1)
            self.mapa.obtener_celda(*vehiculo.ubicacion).ocupantes.append(vehiculo)
            self.vehiculos.append(vehiculo)

        for vehiculo in self.vehiculos:
            print(f"Vehículo {vehiculo.id} en {vehiculo.ubicacion}")

        self.mapa.mostrar_mapa()

    def crear_vehiculo(self):
        self.num_vehiculos_gen += 1
        vehiculo = VehiculoAgent(id=self.num_vehiculos_gen)
        self.mapa.obtener_celda(*vehiculo.ubicacion).ocupantes.append(vehiculo)
        self.vehiculos.append(vehiculo)

    def ejecutar(self, iteraciones):
        """Ejecuta la simulación iteración por iteración."""
        for i in range(iteraciones):
            sleep(1) # 1 segundo entre cada iteración
            print(f"\n--- Iteración {i+1} ---")

            # Asegurar que los semáforos cambian de estado
            for f in range(self.mapa.filas):
                for c in range(self.mapa.columnas):
                    celda = self.mapa.obtener_celda(f,c)
                    if celda.semaforo:
                        celda.semaforo.act()  # Cambia de rojo a verde y viceversa
                        print(f"🚦 Semáforo en {celda.semaforo.ubicacion} está {'🟥' if celda.semaforo.estado == 0 else '🟩'}")

            # Asegurar que los pasos cambian de estado
            for f in range(self.mapa.filas):
                for c in range(self.mapa.columnas):
                    celda = self.mapa.obtener_celda(f,c)
                    if celda.paso:
                        celda.paso.act()  # Cambia de rojo a verde y viceversa
                        print(f"🏁 paso de peatones en {celda.paso.ubicacion} está {'🚶' if celda.paso.estado == 0 else '🏁'}")

            # Los vehículos intentan moverse
            for vehiculo in self.vehiculos:
                data = vehiculo.mover(self.mapa)
                if data == 404: 
                    self.tiempos_parados.append({
                                                    "id":vehiculo.id,
                                                    "tiempo_parado":vehiculo.tiempo_parado
                                                 })
                    self.vehiculos.remove(vehiculo)
                    self.crear_vehiculo()


            # Mostrar el estado del mapa y semáforos
            self.mapa.mostrar_mapa()

        ''' Lectura de estadísticas de tiempos parados'''
        for vehiculo in self.vehiculos:
            self.tiempos_parados.append({
                                        "id":vehiculo.id,
                                        "tiempo_parado":vehiculo.tiempo_parado
                                        })
        max={"id":0,"tiempo_parado":0}
        min={"id":0,"tiempo_parado":10000000}
        mean=0
        for i in self.tiempos_parados:
            if i["tiempo_parado"] > max["tiempo_parado"]:
                max=i
            if i["tiempo_parado"] < min["tiempo_parado"]:
                min=i
            mean+=i["tiempo_parado"]
        mean=mean/len(self.tiempos_parados)
        print("Estadisticas: ")
        print("Se han generado un total de " +str(self.num_vehiculos_gen) + " coches")
        print("Maximo tiempo parado: el coche número " + str(max["id"]) + " ha estado parado " + str(max["tiempo_parado"]) + " segundos")
        print("Minimo tiempo parado: el coche número " + str(min["id"]) + " ha estado parado " + str(min["tiempo_parado"]) + " segundos")
        print("Media tiempo parado: " +str(mean) + " segundos")

# Ejecutar la simulación
if __name__ == "__main__":
    simulacion = Simulacion(17, 35, 15) # se crean 17 filas, 35 columnas y 15 coches al inicio
    simulacion.ejecutar(50) # 50 segundos de simulación
