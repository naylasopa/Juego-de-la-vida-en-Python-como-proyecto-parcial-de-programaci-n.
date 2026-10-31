import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from game_of_life import update, N, ON, OFF

# Título de la aplicación en la web
st.title("🦠 Juego de la Vida de Conway")
st.write("Simulación de autómatas celulares desarrollada con Python y Streamlit.")

# 1. Inicializar el estado del tablero en la memoria de Streamlit (session_state)
if "grid" not in st.session_state:
    # Creamos un tablero inicial con algunas células vivas de ejemplo o aleatorias
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

# 2. Panel de control lateral (Sidebar) para los botones
st.sidebar.header("Controles de Simulación")

# Botón para avanzar una generación (Equivalente a tu botón 'Step')
if st.sidebar.button("Siguiente Generación (Step)"):
    st.session_state.grid = update(st.session_state.grid)

# Botón para limpiar el tablero (Equivalente a tu botón 'Limpiar')
if st.sidebar.button("Limpiar Tablero"):
    st.session_state.grid = np.full((N, N), OFF)

# Botón para reiniciar con un patrón aleatorio
if st.sidebar.button("Generar Patrón Aleatorio"):
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

# 3. Visualización gráfica del tablero usando Matplotlib
fig, ax = plt.subplots(figsize=(6, 6))
# 'cmap="binary"' hace que el 0 sea blanco (muerta) y el 1 sea negro (viva)
ax.imshow(st.session_state.grid, cmap="binary", interpolation="nearest")

# Mostrar las líneas de la cuadrícula para que se vea estético
ax.set_xticks(np.arange(-0.5, N, 1), minor=True)
ax.set_yticks(np.arange(-0.5, N, 1), minor=True)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Renderizar la gráfica dentro de la página web de Streamlit
st.pyplot(fig)