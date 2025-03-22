from time import sleep
from entorno.mapa import Mapa
from agentes.vehiculo import VehiculoAgent
from agentes.semaforo import SemaforoAgent
from agentes.controlador import ControlTraficoAgent

class Simulacion:
    def __init__(self, filas, columnas, num_vehiculos):
        self.mapa = Mapa(filas, columnas)
        self.mapa.inicializar_mapa()
        self.control_trafico = ControlTraficoAgent() 
        self.num_vehiculos_gen = num_vehiculos

        # Crear lista de vehículos
        self.vehiculos = []
        for i in range(num_vehiculos):
            destino = (9, 3)  # Destino del vehículo
            
            # Asegurarse de que la posición inicial es una calle
            vehiculo = VehiculoAgent(id=i+1, destino=destino)
            self.mapa.obtener_celda(*vehiculo.ubicacion).ocupantes.append(vehiculo)
            self.vehiculos.append(vehiculo)

        for vehiculo in self.vehiculos:
            print(f"✅ Vehículo {vehiculo.id} en {vehiculo.ubicacion}, destino {vehiculo.destino}")

        self.mapa.mostrar_mapa()

    def crear_vehiculo(self):
        destino = (9, 3) 
        self.num_vehiculos_gen += 1
        vehiculo = VehiculoAgent(id=self.num_vehiculos_gen, destino=destino)
        self.mapa.obtener_celda(*vehiculo.ubicacion).ocupantes.append(vehiculo)
        self.vehiculos.append(vehiculo)

    def ejecutar(self, iteraciones):
        """Corre la simulación iteración por iteración."""
        for i in range(iteraciones):
            sleep(0.5)
            print(f"\n--- Iteración {i+1} ---")

            # 1️⃣ 🔹 Asegurar que los semáforos cambian de estado
            for f in range(self.mapa.filas):
                for c in range(self.mapa.columnas):
                    celda = self.mapa.obtener_celda(f,c)
                    if celda.semaforo:
                        celda.semaforo.act()  # ✅ Ahora cambia de rojo a verde y viceversa
                        print(f"🚦 Semáforo en {celda.semaforo.ubicacion} está {'🟥' if celda.semaforo.estado == 0 else '🟩'}")

            # 1️⃣ 🔹 Asegurar que los pasos cambian de estado
            for f in range(self.mapa.filas):
                for c in range(self.mapa.columnas):
                    celda = self.mapa.obtener_celda(f,c)
                    if celda.paso:
                        celda.paso.act()  # ✅ Ahora cambia de rojo a verde y viceversa
                        print(f"🚦 paso en {celda.paso.ubicacion} está {'🟥' if celda.paso.estado == 0 else '🟩'}")

            # 2️⃣ 🔹 Los vehículos intentan moverse
            for vehiculo in self.vehiculos:
                data = vehiculo.mover(self.mapa)
                if data == 404:
                    self.vehiculos.remove(vehiculo)
                    self.crear_vehiculo()


            # 3️⃣ 🔹 Mostrar el estado del mapa y semáforos
            self.mapa.mostrar_mapa()

            
                

# Ejecutar la simulación
if __name__ == "__main__":
    simulacion = Simulacion(17, 35, 10)
    simulacion.ejecutar(50)
