from autogen import Agent
import random


class VehiculoAgent(Agent):
    def __init__(self, id):
        entradas_posibles=[(0,1),(0,2),(16,32),(16,33), (2,34),(8,0),(14,0)] # Entradas al mapa

        self.id = id # ID de los coches
        self.ubicacion = entradas_posibles[random.randint(0,6)] # Elección aleatoria de una entrada

        self.p_aparcar_parking = 0.7 # Probabilidad entrar al parking
        self.plazas_parking = 10 # Máximo plazas de parking
        self.p_aparcar = 0.1 # Probabilidad aparcar en la calle
        self.aparcado = 0
        self.ubicacion_desaparcar = None
        self.time_out_aparcar = 0

        self.tiempo_parado = 0

    def act(self, entorno):
        """Consulta al semáforo y decide si moverse."""
        mensaje = f"Estoy en {self.ubicacion}. ¿Puedo moverme?" 
        print(f"🚗 Vehículo {self.id} recibe: {mensaje}")

        self.mover(entorno)


    def mover(self, entorno):
        """Mueve el vehículo hacia adelante, saltando el semáforo si es necesario."""
    
        x, y = self.ubicacion

        if self.aparcado > 0:
            if self.aparcado == 1:
                self.aparcado = 0
                celda_destino = entorno.obtener_celda(*self.ubicacion_desaparcar)
                entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                celda_destino.ocupantes.append(self)  # Mover al nuevo destino
                self.ubicacion = self.ubicacion_desaparcar  # Actualizar posición
                print(f"🚗 Vehículo {self.id} se movió a {self.ubicacion}")
                self.time_out_aparcar = 3
                return  # Salir del bucle al encontrar un movimiento válido
            self.aparcado -= 1
            print(f"🚗 Vehículo {self.id} esta aparcado en {self.ubicacion}")
            return
        
        if entorno.obtener_celda(*self.ubicacion) != None:
            if entorno.obtener_celda(*self.ubicacion).tipo == "interseccion":
                opciones = entorno.obtener_celda(*self.ubicacion).opciones
                sentido = opciones[random.randint(0,len(opciones)-1)]

            elif entorno.obtener_celda(*self.ubicacion).tipo == "calle":
                sentido = entorno.obtener_celda(*self.ubicacion).sentido


        ''' Modelado del aparcamiento del vehiculo '''
        # Si el coche se mueve hacia arriba o hacia abajo, podrá aparcar a la izquierda o a la derecha
        if entorno.obtener_celda(*self.ubicacion).sentido== 0 or entorno.obtener_celda(*self.ubicacion).sentido== 1:
            celda_derecha = entorno.obtener_celda(x, y+1)
            celda_izquierda = entorno.obtener_celda(x, y-1)
            
            # Permite aparcar en la calle derecha al coche
            if celda_derecha.tipo == "plaza" and len(celda_derecha.ocupantes) == 0 and self.time_out_aparcar == 0:
                if random.random() < self.p_aparcar:
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_derecha.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion_desaparcar = self.ubicacion
                    self.ubicacion = (x, y+1)  # Actualizar posición
                    self.aparcado = random.randint(1,6)
                    print(f"🚗 Vehículo {self.id} se aparco en {self.ubicacion}")
                    return
                
            # Permite aparcar en la calle izquierda al coche
            elif celda_izquierda.tipo == "plaza" and len(celda_izquierda.ocupantes) == 0 and self.time_out_aparcar == 0:
                if random.random() < self.p_aparcar:
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_izquierda.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion_desaparcar = self.ubicacion
                    self.ubicacion = (x, y-1)  # Actualizar posición
                    self.aparcado = random.randint(1,6)
                    print(f"🚗 Vehículo {self.id} se aparco en {self.ubicacion}")
                    return

        # Si el coche se mueve hacia la izquierda o hacia la derecha, podrá aparcar arriba o abajo
        if entorno.obtener_celda(*self.ubicacion).sentido== 2 or entorno.obtener_celda(*self.ubicacion).sentido== 3:
            celda_arriba = entorno.obtener_celda(x-1, y)
            celda_abajo = entorno.obtener_celda(x+1, y) 

            # Aparcamiento en parking (arriba segun la situacion del mapa)
            if celda_arriba.tipo == "parking" and len(celda_arriba.ocupantes) < self.plazas_parking and self.time_out_aparcar == 0:
                if random.random() < self.p_aparcar_parking:
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_arriba.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion_desaparcar = self.ubicacion
                    self.ubicacion = (x-1, y) # Actualizar posición
                    self.aparcado = random.randint(3,8)
                    print(f"🅿️ Vehículo {self.id} entro en parking {self.ubicacion}, hay {len(celda_arriba.ocupantes)} de {self.plazas_parking}")
                    return
            # Permite aparcar en la calle de "arriba"
            elif celda_arriba.tipo == "plaza" and len(celda_arriba.ocupantes) == 0 and self.time_out_aparcar == 0:
                if random.random() < self.p_aparcar:
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_arriba.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion_desaparcar = self.ubicacion
                    self.ubicacion = (x-1, y) # Actualizar posición
                    self.aparcado = random.randint(1,6)
                    print(f"🚗 Vehículo {self.id} se aparco en {self.ubicacion}")
                    return
            # Permite aparcar en la calle de "abajo"
            elif celda_abajo.tipo == "plaza" and len(celda_abajo.ocupantes) == 0 and self.time_out_aparcar == 0:
                if random.random() < self.p_aparcar:
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_abajo.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion_desaparcar = self.ubicacion
                    self.ubicacion = (x+1, y)  # Actualizar posición
                    self.aparcado = random.randint(1,6)
                    print(f"🚗 Vehículo {self.id} se aparco en {self.ubicacion}")
                    return
            
        if self.time_out_aparcar > 0:
            self.time_out_aparcar -=1
        
        # Define los posibles movimientos: normal y salto de semáforo
        match sentido:
            case 0:
                posibles_movimientos = [(x + 1, y), (x + 2, y)]  
            case 1:
                posibles_movimientos = [(x -1, y), (x - 2, y)]  
            case 2:
                posibles_movimientos = [(x, y + 1), (x, y + 2)]  
            case 3:
                posibles_movimientos = [(x, y - 1), (x, y - 2)]  

        nx, ny = posibles_movimientos[0]
        celda_destino = entorno.obtener_celda(nx, ny)
        if celda_destino != None:
            if celda_destino.semaforo!= None:
                if celda_destino.semaforo.estado == 0:
                    self.tiempo_parado += 1
                    print(f"🚗 Vehículo {self.id} espera en {self.ubicacion}, semáforo rojo.")
                    return  # No se mueve si el semáforo está en rojo
                else:
                    nx, ny = posibles_movimientos[1]
                    celda_destino = entorno.obtener_celda(nx, ny)
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_destino.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion = (nx, ny)  # Actualizar posición
                    print(f"🚗 Vehículo {self.id} se movió a {self.ubicacion}")
                    return  # Salir del bucle al encontrar un movimiento válido
            if celda_destino.paso!= None:
                if celda_destino.paso.estado == 1:
                    self.tiempo_parado += 1
                    print(f"🚗 Vehículo {self.id} espera en {self.ubicacion}, por peatón.")
                    return  # No se mueve si el semáforo está en rojo
                else:
                    nx, ny = posibles_movimientos[1]
                    celda_destino = entorno.obtener_celda(nx, ny)
                    entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                    celda_destino.ocupantes.append(self)  # Mover al nuevo destino
                    self.ubicacion = (nx, ny)  # Actualizar posición
                    print(f"🚗 Vehículo {self.id} se movió a {self.ubicacion}")
                    return  # Salir del bucle al encontrar un movimiento válido
                    
            if not celda_destino.ocupantes:  # Solo avanza si la celda está libre
                entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
                celda_destino.ocupantes.append(self)  # Mover al nuevo destino
                self.ubicacion = (nx, ny)  # Actualizar posición
                print(f"🚗 Vehículo {self.id} se movió a {self.ubicacion}")
                return  # Salir del bucle al encontrar un movimiento válido
        else:
            entorno.obtener_celda(x, y).ocupantes.remove(self)  # Quitar de la celda actual
            print(f"🚗 Vehículo {self.id} ha salido.")  # Si no puede moverse
            return 404   
        self.tiempo_parado += 1
        print(f"🚗 Vehículo {self.id} está bloqueado en {self.ubicacion}")  # Si no puede moverse






