import matplotlib.pyplot as plt
import numpy as np

def draw_board(board):
    # Creamos la figura
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # Dibujamos la matriz (0 = muerto, 1 = vivo)
    # Usamos el mapa de colores 'Greens' (blanco para muertos, verde para vivos)
    ax.imshow(board, cmap='Greens', vmin=0, vmax=1)
    
    # Dibujamos las líneas de la cuadrícula
    ax.set_xticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(board), 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
    
    # Quitamos los números de los ejes para que se vea limpio
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig