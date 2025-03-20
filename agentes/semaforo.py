from autogen import Agent

class SemaforoAgent:
    """Agente que controla un semáforo en una intersección."""
    def __init__(self, ubicacion, tiempo_rojo, tiempo_verde):
        self.ubicacion = ubicacion
        self.tiempo_rojo = tiempo_rojo
        self.tiempo_verde = tiempo_verde
        self.estado = "rojo"
        self.tiempo_actual = 0

    def act(self):
        """Cambia el estado del semáforo después del tiempo especificado."""
        self.tiempo_actual += 1
        if self.estado == "rojo" and self.tiempo_actual >= self.tiempo_rojo:
            self.estado = "verde"
            self.tiempo_actual = 0  # Reinicia el contador
        elif self.estado == "verde" and self.tiempo_actual >= self.tiempo_verde:
            self.estado = "rojo"
            self.tiempo_actual = 0  # Reinicia el contador

