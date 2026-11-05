import time
import numpy as np
import streamlit as st
from game_logic import update, N, ON, OFF
#vane agregue:
from visualization import draw_board

st.title("Juego de la Vida")

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

# Botones de control
c1, c2, c3, c4, c5 = st.columns(5)
c1.button("Comenzar", on_click=start, use_container_width=True)
c2.button("Parar", on_click=stop, use_container_width=True)
c3.button("Step", on_click=step, use_container_width=True)
c4.button("Limpiar", on_click=clear, use_container_width=True)
speed = c5.selectbox("Velocidad", list(speed_dict.keys()), index=1, label_visibility="collapsed")

# Cuadrícula de botones (Usando la funcion de estudiante B: Vane)
fig = draw_board(st.session_state.grid)
st.pyplot(fig)

# Animación 
if st.session_state.running:
    time.sleep(speed_dict[speed])
    step()
    st.rerun()