from autogen import Agent

class VehiculoAgent(Agent):
    def __init__(self, id, ubicacion, destino):
        super().__init__(
            name=f"Vehiculo_{id}",
            system_message="Eres un vehículo que navega por una ciudad."
        )
        self.id = id
        self.ubicacion = ubicacion
        self.destino = destino

    def act(self, entorno, control_trafico):
        mensaje = f"Estoy en {self.ubicacion}. ¿Puedo moverme?"
        respuesta = self.send(mensaje, recipient=control_trafico)
        print(f"🚗 Vehículo {self.id} recibe: {respuesta}")

