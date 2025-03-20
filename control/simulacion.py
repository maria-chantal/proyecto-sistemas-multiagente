from entorno.mapa import Mapa
from agentes.vehiculo import VehiculoAgent
from agentes.semaforo import SemaforoAgent
from agentes.controlador import ControlTraficoAgent

class Simulacion:
    def __init__(self, filas, columnas, num_vehiculos):
        self.mapa = Mapa(filas, columnas)
        self.mapa.inicializar_mapa()
        self.control_trafico = ControlTraficoAgent()  # ✅ Se crea correctamente
        self.vehiculos = [VehiculoAgent(i, (0, 3), (9, 3)) for i in range(num_vehiculos)]
        self.semaforos = [SemaforoAgent((5, 3), 5, 5)]

        
        # Crear lista de vehículos
        self.vehiculos = []
        for i in range(num_vehiculos):
            inicio = (0, 3)  # Posición inicial en una calle
            destino = (9, 3)  # Destino del vehículo
            
            # Asegurarse de que la posición inicial es una calle
            if self.mapa.obtener_celda(*inicio) and self.mapa.obtener_celda(*inicio).tipo == "calle":
                vehiculo = VehiculoAgent(id=i, ubicacion=inicio, destino=destino)
                self.vehiculos.append(vehiculo)
                self.mapa.obtener_celda(*inicio).ocupantes.append(vehiculo)  # Agregar al mapa
            else:
                print(f"⚠️ No se pudo colocar el vehículo {i} en {inicio}, no es una calle.")
        for vehiculo in self.vehiculos:
            print(f"✅ Vehículo {vehiculo.id} en {vehiculo.ubicacion}, destino {vehiculo.destino}")

        self.semaforos = [SemaforoAgent((5, 3), 5, 5)]

    def ejecutar(self, iteraciones):
        """Corre la simulación durante el número de iteraciones dado."""
        for i in range(iteraciones):
            print(f"\n--- Iteración {i+1} ---")

            # 1️⃣ Los semáforos cambian de estado
            for semaforo in self.semaforos:
                semaforo.act()

            # 2️⃣ Los vehículos intentan moverse
            for vehiculo in self.vehiculos:
                vehiculo.act(self.mapa, self.control_trafico)

            # 3️⃣ Mostrar estado de los semáforos
            for semaforo in self.semaforos:
                print(f"🚦 Semáforo en {semaforo.ubicacion} está {semaforo.estado}")

    def ejecutar(self, iteraciones):
        """Corre la simulación iteración por iteración."""
        for i in range(iteraciones):
            input("\n🔄 Presiona ENTER para avanzar a la siguiente iteración...")  # Espera ENTER
            print(f"\n--- Iteración {i+1} ---")

            # 1️⃣ Asegurar que los semáforos cambian de estado
            for semaforo in self.semaforos:
                semaforo.act()

            # 2️⃣ Los vehículos intentan moverse (🔹 Ahora pasamos `self.control_trafico`)
            for vehiculo in self.vehiculos:
                vehiculo.act(self.mapa, self.control_trafico)  # ✅ Corrección aquí

            # 3️⃣ Mostrar el estado del mapa y semáforos
            self.mapa.mostrar_mapa()

            # 4️⃣ Mostrar el estado de los semáforos
            for semaforo in self.semaforos:
                print(f"🚦 Semáforo en {semaforo.ubicacion} está {'🟥' if semaforo.estado == 'rojo' else '🟩'}")

# Ejecutar la simulación
if __name__ == "__main__":
    simulacion = Simulacion(10, 10, 3)
    simulacion.ejecutar(10)
