import time
import numpy as np
import streamlit as st

from game_logic import update, N, ON, OFF
#vane agregue:
from visualization import draw_board

st.title("Juego de la Vida")
#.update(): este calcula la siguiente generacion
#N: tamaño del tablero, ON: celula viva(1), OFF: celula muerta(0)
from patterns import create_glider

# Estado 
if "grid" not in st.session_state:
    st.session_state.grid = np.full((N, N), OFF)
if "running" not in st.session_state:
    st.session_state.running = False

speed_dict = {"Lento": 0.5, "Normal": 0.2, "Rápido": 0.1, "Rapidito": 0.05, "MaxJoputa": 0.01}

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
    st.session_state.grid = np.random.choice([ON, OFF], size=(N, N), p=[0.2, 0.8])

# Glider: genera un planeador en el tablero
if st.sidebar.button("Crear Glider"):
    st.session_state.running = False
    st.session_state.grid = create_glider()

# Cuadrícula de botones (Usando la funcion de estudiante B: Vane)
fig = draw_board(st.session_state.grid)
st.pyplot(fig)

# Animación 
if st.session_state.running:
    time.sleep(speed_dict[speed])

    step()
    st.rerun()

#Explicacion rapida de algunos conceptos "nuevos" que estuvimos aprendiendo
#1.session_state: guarda el tablero porque Streamlit se vuelve a ejecutar completo con cada clic.
#2.st.rerun(): es lo que hace que la animación avance sola.
#3.update(): viene del archivo de mi compañera que es A.
