from entorno.mapa import Mapa
from agentes.vehiculo import VehiculoAgent
from agentes.semaforo import SemaforoAgent
from agentes.controlador import ControlTraficoAgent


class Simulacion:
    """Ejecuta la simulación iterando sobre los agentes."""
    
    def __init__(self, filas, columnas, num_vehiculos):
        self.mapa = Mapa(filas, columnas)
        self.mapa.inicializar_mapa()
        self.vehiculos = [VehiculoAgent(i, (0, 3), (9, 3)) for i in range(num_vehiculos)]
        self.semaforos = [SemaforoAgent((5, 3), 5, 5)]
    
    

    
    
    def ejecutar(self, iteraciones):
        control_trafico = ControlTraficoAgent()
        """Corre la simulación durante el número de iteraciones dado."""
        for i in range(iteraciones):
            print(f"\n--- Iteración {i+1} ---")

            # 1️⃣ Los semáforos cambian de estado
            for semaforo in self.semaforos:
                semaforo.act()

            # 2️⃣ Los vehículos intentan moverse
            for vehiculo in self.vehiculos:
                vehiculo.act(self.mapa, control_trafico)  # Ahora los vehículos consultan al controlador

            # 3️⃣ Mostrar estado de los semáforos
            for semaforo in self.semaforos:
                print(f"Semáforo en {semaforo.ubicacion} está {semaforo.estado}")

# Ejecutar la simulación
if __name__ == "__main__":
    simulacion = Simulacion(10, 10, 3)
    simulacion.ejecutar(10)

