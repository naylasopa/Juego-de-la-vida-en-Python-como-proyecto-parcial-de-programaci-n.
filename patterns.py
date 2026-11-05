import numpy as np # Permite trabajar con matrices.
from game_logic import N, ON, OFF # Reutiliza las constantes del código.


def create_glider(size=N, row=1, col=1): # Es la función que genera el planeador.
    """
    Genera un planeador (glider) dentro de un tablero cuadrado.

    Parámetros:
    size: tamaño del tablero.
    row: fila inicial del patrón.
    col: columna inicial del patrón.

    Regresa:
    Un tablero con cinco células vivas formando un planeador.
    """

    if size < 3:
        raise ValueError("El tablero debe tener al menos 3 filas y columnas.")

    # Creamos un tablero inicialmente vacío.
    # np.full(): crea un tablero de 10 x 10 inicialmente con todas las células apagadas.
    grid = np.full((size, size), OFF, dtype=int)

    # Posiciones de las cinco células vivas del planeador.
    glider_cells = [
        (0, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2)
    ]

    # Colocamos las células vivas en el tablero.
    for r, c in glider_cells:
        if row + r >= size or col + c >= size or row < 0 or col < 0:
            raise ValueError("El planeador no cabe en la posición indicada.")

        grid[row + r, col + c] = ON

    return grid # Devuelve el tablero con el patrón generado. 
