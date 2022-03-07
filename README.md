# Calculo de Fuel
Es una pequeña aplicación creada para ayudar a obtener la cantidad de combustible necesaria en **Assetto Corsa Competizione** de forma rapida y sencilla.

![alt text](https://i.imgur.com/F8DRSal.png)



## Como usarla

| Campo Requerido | Descripción |
| ----------- | ----------- |
| Lap Time | Debe introducirse el tiempo de tu mejor vuelta expresada em minutos, segundos y milisegundos. Ej: 1.50.200 |
| Fuel p/ Lap | Debe introducirse el consumo que se muestra luego de dar 3 o 4 vueltas al circuito durante la practica o clasificación. Ej: 6.21|
| Race Duration | Debe introducirse el tiempo en minutos que dura la carrera Ej: 20|

## Instalación

Para que el archivo .py pueda mostrar la aplicacion sera necesario instalar algunos packages, por lo que deberemos seguir los siguientes pasos:

1. Instalar [pip](https://pypi.org/project/pip/)
2. Abrir inicio de windows y excribir "cmd".
3. Click derecho sobre "Command Prompt" y elegir la opcion "Abrir como administrador"
4. Introducir las lineas de comandos que se mustran a continuacion:

- pip install tk
- pip install Pillow

### Tkinter
[Este paquete](https://docs.python.org/es/3/library/tkinter.html) nos permite crear el frame y componentes para poder usar nuestra aplicacion.
```python
from tkinter import *
```


### Pillow
[Este paquete](https://pillow.readthedocs.io/en/stable/) se encarga de que podamos manipular las imagen que se muestra de fondo.
```python
from PIL import Image, ImageTk
```

### Winsound
[Este paquete](https://docs.python.org/3/library/winsound.html) lo utilizamos para reproducir sonidos luego de clickear el boton "Calculate".
```python
from winsound import *
```


