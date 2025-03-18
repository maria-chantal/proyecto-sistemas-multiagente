from autogen import Agent

class ControlTraficoAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ControlTrafico",
            system_message="Eres el agente que gestiona el tráfico urbano."
        )

    def recibir_mensaje(self, mensaje):
        print(f"📩 Mensaje recibido: {mensaje}")
        return "Puedes avanzar" if "moverme" in mensaje else "Espera"
