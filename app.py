import time #Para pausar entre generaciones (velocidad de la animacion)
import streamlit as st #Libreria de la pagina web
import numpy as np #Para manejar el tablero como matriz
import matplotlib.pyplot as plt #Para dibujar el tablero como imagen

#next_generation: este calcula la siguiente generacion
#N: tamaño del tablero, ON: celula viva(1), OFF: celula muerta(0)
from game_logic import next_generation, N, ON, OFF

# Título y descripcion que se ven en la parte de arriba de la pagina
st.title(" Juego de la Vida de Conway")
st.write("Simulación de autómatas celulares desarrollada con Python y Streamlit.")

# 1. Inicializar el estado del tablero en la memoria de Streamlit (session_state)
#'grid' es el tablero
if "grid" not in st.session_state:
    # Creamos un tablero inicial con algunas células vivas de ejemplo o aleatorias
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

#'running' nos va a indicar si la animacion automatica esta activada o no
if "running" not in st.session_state:
    st.session_state.running = False

#En esta parte vamos agregar las velocidades, seria el nombre y segundos de espera entre generaciones
speed_dict = {"Lento": 0.5, "Normal": 0.2, "Rapido": 0.1, "Rapidito": 0.05, "MaxJoputa": 0.01 }

# 2. Panel de control lateral (Sidebar) para los botones
#Cada boton cambia el estado del juego cuando se le da clic
st.sidebar.header("Controles de Simulación")

# Comenzar: activa la animación automática
if st.sidebar.button(" Comenzar"):
    st.session_state.running = True

# Parar: detiene la animación automática
if st.sidebar.button(" Parar"):
    st.session_state.running = False

# Step: avanza una sola generación (usa la función de mi compañera que realizo la parte A)
if st.sidebar.button("Siguiente Generación (Step)"):
    st.session_state.grid = next_generation(st.session_state.grid)

# Limpiar: detiene la animación y deja todas las células muertas
if st.sidebar.button("Limpiar Tablero"):
    st.session_state.running = False
    st.session_state.grid = np.full((N, N), OFF)

# Aleatorio: genera un nuevo tablero con células vivas al azar
if st.sidebar.button("Generar Patrón Aleatorio"):
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

# Selector de velocidad de la animación
speed = st.sidebar.selectbox("Velocidad", list(speed_dict.keys()), index=1)

# 3. Visualización gráfica del tablero (Matplotlib)
fig, ax = plt.subplots(figsize=(6, 6))

# 'cmap="binary"' hace que el 0 sea blanco (muerta) y el 1 sea negro (viva)
ax.imshow(st.session_state.grid, cmap="binary", interpolation="nearest")

#Líneas de la cuadrícula para que se vea cada celda
ax.set_xticks(np.arange(-0.5, N, 1), minor=True)
ax.set_yticks(np.arange(-0.5, N, 1), minor=True)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Renderizar la gráfica dentro de la página web de Streamlit
st.pyplot(fig)

# 4. Editor para poder dibujar las celdas a mano
# Solo aparece cuando la animación está detenida
if not st.session_state.running:
    with st.expander("Editar células a mano"):
        # Mostramos el tablero como tabla de casillas (True = viva, False = muerta)
        editado = st.data_editor(
            st.session_state.grid.astype(bool),
            hide_index=True,
            key="editor",
        )
        # Al dar clic, convertimos las casillas de vuelta a 1 y 0 y actualizamos el tablero
        if st.button("Aplicar cambios"):
            st.session_state.grid = np.where(editado.to_numpy(), ON, OFF)
            st.rerun()

# 5. Animacion automatica
# Si 'running' está activo: espera, avanza una generación y vuelve a ejecutar la página
if st.session_state.running:
    time.sleep(speed_dict[speed])
    st.session_state.grid = next_generation(st.session_state.grid)
    st.rerun()

#Explicacion rapida:
#session_state: guarda el tablero porque Streamlit se vuelve a ejecutar completo con cada clic.
#st.rerun(): es lo que hace que la animación avance sola.
#next_generation: viene del archivo de mi compañera que es A.
