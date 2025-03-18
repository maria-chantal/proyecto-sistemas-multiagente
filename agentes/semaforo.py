from autogen import Agent

class SemaforoAgent(Agent):
    def __init__(self, ubicacion, tiempo_verde, tiempo_rojo):
        super().__init__(
            name=f"Semaforo_{ubicacion}",
            system_message="Regulas el tráfico en una intersección cambiando entre rojo y verde.",
            description="Agente que controla el flujo del tráfico."
        )
        self.ubicacion = ubicacion
        self.tiempo_verde = tiempo_verde
        self.tiempo_rojo = tiempo_rojo
        self.estado = "rojo"
        self.contador = 0

    def act(self):
        """Alterna entre rojo y verde."""
        self.contador += 1
        if self.estado == "rojo" and self.contador >= self.tiempo_rojo:
            self.estado = "verde"
            self.contador = 0
        elif self.estado == "verde" and self.contador >= self.tiempo_verde:
            self.estado = "rojo"
            self.contador = 0
