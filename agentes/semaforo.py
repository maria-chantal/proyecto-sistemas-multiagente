from autogen import Agent

class SemaforoAgent:
    """Agente que controla un semáforo en una intersección."""
    semaforos_globales = {}
    def __init__(self, ubicacion, tiempo_rojo, tiempo_verde):
        self.id = 1
        self.ubicacion = ubicacion
        self.tiempo_rojo = tiempo_rojo
        self.tiempo_verde = tiempo_verde
        self.estado = 0
        self.tiempo_actual = 0
        SemaforoAgent.semaforos_globales[ubicacion] = self  


    def act(self):
        """Cambia el estado del semáforo después del tiempo especificado."""
        self.tiempo_actual += 1
        if self.estado == 0 and self.tiempo_actual >= self.tiempo_rojo:
            self.estado = 1 # Semáforo verde
            self.tiempo_actual = 0  # Reinicia el contador
        elif self.estado == 1 and self.tiempo_actual >= self.tiempo_verde:
            self.estado = 0 # Semáforo rojo
            self.tiempo_actual = 0  # Reinicia el contador



