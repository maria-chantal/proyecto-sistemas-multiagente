from autogen import Agent
import random

class PasoPeatonesAgent(Agent):
    def __init__(self, ubicacion):
        super().__init__()
        self.ubicacion = ubicacion
        self.tiempo_espera =1
        self.estado = 0

    def act(self):
        """Activa o desactiva el cruce de peatones aleatoriamente."""
        if random.random() < 0.3:  # 30% de probabilidad de activación
            self.estado = 1 # Peatón cruzando
        else:
            self.estado = 0 # Paso de peatones vacío
