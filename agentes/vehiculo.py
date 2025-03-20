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
        """Consulta al semáforo y decide si moverse."""
        mensaje = f"Estoy en {self.ubicacion}. ¿Puedo moverme?"
        respuesta = control_trafico.recibir_mensaje(mensaje)  # ✅ Ahora usa el agente de control

        print(f"🚗 Vehículo {self.id} recibe: {respuesta}")

        if respuesta == "Puedes avanzar":
            self.mover(entorno)

    
    def mover(self, entorno):
        """Mueve el vehículo hacia adelante solo si el semáforo está en verde."""
        x, y = self.ubicacion
        dx = 1 if self.destino[0] > x else -1 if self.destino[0] < x else 0  # Movimiento en X
        dy = 1 if self.destino[1] > y else -1 if self.destino[1] < y else 0  # Movimiento en Y

        # Priorizar movimiento hacia adelante
        posibles_movimientos = [(x + dx, y), (x, y + dy)]

        for nx, ny in posibles_movimientos:
            celda_destino = entorno.obtener_celda(nx, ny)
            if celda_destino and celda_destino.tipo == "calle":
                # 🔹 Solo verificamos el semáforo si la celda realmente tiene uno
                if hasattr(celda_destino, "semaforo") and celda_destino.semaforo:
                    if celda_destino.semaforo.estado == "rojo":
                        print(f"🚗 Vehículo {self.id} espera en {self.ubicacion}, semáforo rojo.")
                        return  # No se mueve si el semáforo está en rojo

                if not celda_destino.ocupantes:  # Solo avanza si la celda está libre
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_destino.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion = (nx, ny)  # Actualizar posición
                    print(f"🚗 Vehículo {self.id} se movió a {self.ubicacion}")
                    return  # Salir del bucle al encontrar un movimiento válido

        print(f"🚗 Vehículo {self.id} está bloqueado en {self.ubicacion}")  # Si no puede moverse






