from autogen import Agent
import random

class PasoPeatonesAgent(Agent):
    def __init__(self, ubicacion, tiempo_espera):
        super().__init__()
        self.ubicacion = ubicacion
        self.tiempo_espera = tiempo_espera
        self.estado = "inactivo"

    def act(self):
        """Activa o desactiva el cruce de peatones aleatoriamente."""
        if random.random() < 0.3:  # 30% de probabilidad de activación
            self.estado = "activo"
        else:
            self.estado = "inactivo"
