import numpy as np
from game_logic import N, ON, OFF, update
from patterns import create_glider


def test_stable_block():
    # Creamos un tablero vacío.
    grid = np.full((N, N), OFF, dtype=int)

    # Colocamos cuatro células vivas formando un bloque.
    grid[4:6, 4:6] = ON

    # Calculamos la siguiente generación.
    new_grid = update(grid)

    # Comprobamos que el bloque permanezca igual.
    assert np.array_equal(grid, new_grid)


def test_glider_has_five_live_cells():
    # Generamos un planeador.
    grid = create_glider()

    # Comprobamos que tenga exactamente cinco células vivas.
    assert np.sum(grid == ON) == 5
