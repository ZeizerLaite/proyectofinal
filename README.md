#Tic Tac Toe

##Datos

**Nombre:** Gabriel Alfaro Salcedo  
**Matrícula:** A01621546  
**Juego seleccionado:** Tic Tac Toe

##Descripción

El proyecto consiste en modificar el videojuego Tic Tac Toe de la
biblioteca Free Python Games.

Primero se ejecutó y analizó el código original para comprender cómo
se dibujaban el tablero y los símbolos y cómo se alternaban los turnos.

Después se realizaron las modificaciones solicitadas de manera
independiente y cada versión funcional se almacenó mediante un commit.

## Código original

El código original contiene las funciones `grid()`, `drawx()`,
`drawo()`, `floor()` y `tap()`.

La función `grid()` dibuja el tablero.

Las funciones `drawx()` y `drawo()` dibujan los símbolos de los
jugadores.

La función `floor()` convierte las coordenadas de un clic en las
coordenadas correspondientes a una casilla.

La función `tap()` recibe cada clic, dibuja el símbolo del jugador
actual y posteriormente cambia el turno.

Originalmente el programa no almacenaba el contenido de las casillas,
por lo que era posible volver a seleccionar una posición utilizada.
Tampoco comprobaba si existía un ganador o si la partida terminaba
en empate.

## Modificación 1: personalización de X y O

Se modificaron el color, grosor, tamaño y posición de los símbolos.

La X se cambió a color azul y se aumentó el grosor de sus líneas.

También se agregó un margen para evitar que sus líneas tocaran los
bordes de la casilla y para mantener el símbolo centrado.

La O se cambió a color rojo y se modificó su radio.

Para centrarla se calculó el centro de la casilla y se posicionó la
tortuga en el punto desde el cual debe comenzar a dibujarse el círculo.

## Modificación 2: validación de casillas

Se agregó una lista llamada `board` con nueve elementos.

Cada elemento representa una posición del tablero.

Inicialmente las nueve posiciones contienen `None`, lo que representa
una casilla disponible.

Se agregó la función `square_index()` para convertir las coordenadas
seleccionadas por el usuario en una posición del tablero entre 0 y 8.

Antes de dibujar un símbolo, el programa comprueba si la posición
seleccionada contiene `None`.

Si la posición ya está ocupada, el clic se ignora y el turno no cambia.

Si está disponible, la jugada se dibuja y posteriormente se almacena
en `board`.

##Modificación 3: victoria y empate

Se agregó la función `check_winner()`.

Esta función almacena y revisa las ocho posibles combinaciones
ganadoras:

- Tres filas.
- Tres columnas.
- Dos diagonales.

Después de cada movimiento se comprueba si las tres posiciones de
alguna combinación contienen al mismo jugador.

Cuando esto ocurre se muestra si ganó X o si ganó O.

También se agregó la función `board_is_full()`.

Esta función comprueba si las nueve posiciones están ocupadas.

Si el tablero está lleno y no existe un ganador, la partida termina
en empate.

Finalmente se agregó `finished` al estado del juego.

Cuando existe una victoria o un empate, `finished` cambia a `True`
para impedir movimientos adicionales.

##Comentarios en el código

Se agregaron comentarios para explicar las partes principales de las
modificaciones realizadas.

Se mantuvo el idioma del código original.

Los comentarios explican el centrado de los símbolos, el estado del
tablero, la conversión de coordenadas, la validación de las casillas,
las combinaciones ganadoras, la detección del empate y la finalización
de la partida.

##Proceso con Git

El desarrollo se realizó en la rama:

`A01621546_tictactoe`

La rama fue creada desde `main`.

Se utilizaron commits independientes para conservar una versión
funcional después de cada modificación.

Los commits corresponden a:

1. Versión inicial del juego.
2. Personalización y centrado de los símbolos.
3. Validación de casillas ocupadas.
4. Detección de victoria y empate.
5. Comentarios en el código.

Cada versión fue ejecutada y probada antes de realizar el commit.

Una vez terminadas las modificaciones, la rama se integró nuevamente
a `main`.

##Instalación

Crear el entorno virtual:

```bat
python -m venv .venv
```

Activarlo en Windows:

```bat
.venv\Scripts\activate.bat
```

Instalar Freegames:

```bat
python -m pip install freegames
```

##Ejecución

```bat
python tictactoe.py
```

##Pruebas realizadas

Se comprobó el funcionamiento de X y O.

Se verificó el color, tamaño y centrado de ambos símbolos.

Se intentó seleccionar una casilla ocupada para comprobar que la
jugada fuera rechazada.

Se probaron victorias horizontales, verticales y diagonales.

Se comprobaron victorias tanto de X como de O.

También se realizó una partida que terminara en empate.

Finalmente se comprobó que no fuera posible continuar jugando después
de una victoria o un empate.

##Repositorio

https://github.com/ZeizerLaite/proyectofinal