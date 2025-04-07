# Introducción
Este es el trabajo práctico para la asignatura Sistemas Multiagente realizado por María Chantal. Si se prefiere, puedes encontrar el proyecto en Github: https://github.com/maria-chantal/proyecto-sistemas-multiagente

# Entorno

He instalado los paquetes de Autogen dentro de un entorno virtual venv para evitar problemas con dependencias. 
Para poder activar este entorno, sería necesario activarlo dentro de 
```
autogen_env/Scripts/.activate
```

# Simulación
La simulación se ejecuta desde la clase Simulacion dentro de la carpeta control.
Para inicializar la simulación, se debe usar este comando en terminal
```
python -m control.simulacion
```

# Funcionamiento
La simulación constará de una cuadrícula de 17 filas por 25 columnas. Comenzará generando 15 coches en alguna de las entradas aleatorias. 

Es posible que se generen varios coches dentro de una misma entrada, en este caso, se seguirá un órden nominal en el cual el número más bajo tendrá prioridad de movimiento
y los siguientes esperarán a encontrar un espacio vacío para moverse. 

Todos los semáforos están sincronizados, y los pasos de cebra tienen una probabilidad del 30% de activarse.

Los vehículos pueden aparcar en todas direcciones en las plazas de la calle y existirá un 10% de probabilidades de que decida aparcar. Una vez aparcados, estarán en ese 
estado durante un número aleatorio de turnos (entre 1 y 6 turnos)
En cuanto al parking, exisitrá un 70% de probabilidades de entrar. Una vez dentro del parking, permanecerán dentro un número aleatorio de turnos (entre 3 y 8 turnos).
Al desaparacar, los coches volverán a la misma casilla desde la que entraron.  

Existen 7 posibles entradas aleatorias. Si el coche quiere moverse en una dirección donde no encuentra una celda de destino, se asume que sale del mapa. En este momento, 
dicho coche se eliminará y se generará uno nuevo automáticamente. 

# Obstaculos

Los coches tendrán que esperar si se encuentran un semáforo en rojo o un paso de peatones activado. 

Si un coche quiere desaparcar pero actualmente hay otro coche en la casilla desde la que entró, el coche aparcado tendrá que esperar a que ese espacio se libere. 

Al entrar en una intersección, los coches tienen que pisar primero la intersección antes de decidir su siguiente movimiento. 

# Logs

He decidido guardar la salida generada en un txt para una mejor visualización de la simulación. De esta forma, se puede ver de manera ordenada el funcionamiento
y la interacción de los agentes con el entorno. Este archivo se reescribirá con cada ejecución de la simulación.


