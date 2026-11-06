import time #Para pausar entre generaciones (velocidad de la animacion)
import numpy as np  #Para manejar el tablero como matriz
import streamlit as st #Libreria de la pagina web

from game_logic import update, N, ON, OFF
#vane agregue:
from visualization import draw_board
from patterns import create_glider

#.update(): este calcula la siguiente generacion
#N: tamaño del tablero, ON: celula viva(1), OFF: celula muerta(0)
# Título y descripcion que se ven en la parte de arriba de la pagina
st.title(" Juego de la Vida de Conway")
st.write("Simulación de autómatas celulares desarrollada con Python y Streamlit.")

# 1. Inicializar el estado del tablero en la memoria de Streamlit (session_state)
#'grid' es el tablero
if "grid" not in st.session_state:
    # Creamos un tablero inicial con algunas células vivas de ejemplo o aleatorias
    st.session_state.grid = np.random.choice([ON, OFF], size = (N, N), p = [0.2, 0.8])

#'running' nos va a indicar si la animacion automatica esta activada o no
if "running" not in st.session_state:
    st.session_state.running = False

#En esta parte vamos agregar las velocidades, seria el nombre y segundos de espera entre generaciones
speed_dict = {"Lento": 0.5, "Normal": 0.2, "Rapido": 0.1, "Rapidito": 0.05, "MaxJoputa": 0.01 }

def toggle(i, j):
    g = st.session_state.grid
    g[i, j] = ON if g[i, j] == OFF else OFF

def start():
    st.session_state.running = True

def stop():
    st.session_state.running = False

def step():
    st.session_state.grid = update(st.session_state.grid)

def clear():
    st.session_state.running = False
    st.session_state.grid = np.full((N, N), OFF)
    
# Botones de control en el panel lateral izquierdo
st.sidebar.header("Controles de Simulación")

c1 = st.sidebar
c2 = st.sidebar
c3 = st.sidebar
c4 = st.sidebar
c5 = st.sidebar
c6 = st.sidebar

c1.button("Comenzar", on_click=start, use_container_width=True)
c2.button("Parar", on_click=stop, use_container_width=True)
c3.button("Step", on_click=step, use_container_width=True)
c4.button("Limpiar", on_click=clear, use_container_width=True)

# Selector de velocidad
speed = c5.selectbox(
    "Velocidad", 
    list(speed_dict.keys()), 
    index=1, 
    label_visibility="collapsed"
    )

# Aleatorio: genera un nuevo tablero con células vivas al azar
if c6.button("Generar Patrón Aleatorio", use_container_width=True):
    st.session_state.running = False
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

# Glider: genera un planeador en el tablero
if st.sidebar.button("Crear Glider"):
    st.session_state.running = False
    st.session_state.grid = create_glider()
    
# 3. Visualización gráfica del tablero
fig = draw_board(st.session_state.grid)
st.pyplot(fig) # Renderizar la gráfica dentro de la página web de Streamlit

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
            st.session_state.grid = np.where(editado, ON, OFF)
            st.rerun()

# 5. Animacion automatica
# Si 'running' está activo: espera, avanza una generación y vuelve a ejecutar la página
if st.session_state.running:
    time.sleep(speed_dict[speed])
    step()
    st.rerun()

#Explicacion rapida de algunos conceptos "nuevos" que estuvimos aprendiendo
#1.session_state: guarda el tablero porque Streamlit se vuelve a ejecutar completo con cada clic.
#2.st.rerun(): es lo que hace que la animación avance sola.
#3.update(): calcula la siguiente generación del tablero. 
