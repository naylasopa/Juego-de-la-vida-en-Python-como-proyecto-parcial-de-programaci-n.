import tkinter as tk
import numpy as np
from game_of_life import update, grid, N, ON, OFF

root = tk.Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.resizable(0,0)

def on_click(i, j, grid, buttons):
    grid[i,j] = 1 if grid[i,j] == 0 else 0
    buttons[i][j].config(bg='black' if grid[i,j] else 'white')

buttons= []
for i in range(N):
    row = []
    for j in range(N):
        button = tk.Button(
            root,
            command= lambda i=i, j=j: on_click(i, j, grid, buttons),
            height= 2,
            width= 4,
            bg = 'black' if grid[i,j] else 'white'
        )
        row.append(button)
    buttons.append(row)

for i in range(N):
    for j in range(N):
        buttons[i][j].grid(row=i, column=j, sticky="nsew")

def gui_update():
    global grid
    grid = update(grid)
    for i in range(N):
        for j in range(N):
            buttons[i][j].config(bg='black' if grid[i,j] else 'white')
    if running:
        root.after(speed_dict[speed_var.get()], gui_update)

def start():
    global running
    running = True
    gui_update()

def stop():
    global running
    running = False

def step():
    if not running:
        gui_update()

def clear():
    global grid
    stop()
    grid = np.full((N,N), OFF)
    for i in range(N):
            for j in range(N):
                buttons[i][j].config(bg='black' if grid[i,j] else 'white')
    
            

start_button = tk.Button(root, text='Comenzar' , command = lambda: start())
start_button.grid(row=N, column = 0, columnspan=N//5, sticky="we") 

stop_button = tk.Button(root, text='Parar', command = lambda: stop() )
stop_button.grid(row=N, column = N//5, columnspan=N//5, sticky="we")

step_button = tk.Button(root, text='Step', command = lambda: step())
step_button.grid(row=N, column = 2*N//5, columnspan=N//5, sticky="we") 

clear_button = tk.Button(root, text='Limpiar', command = lambda: clear())
clear_button.grid(row=N, column = 3*N//5, columnspan=N//5, sticky="we") 

speed_dict = {'Lento': 500, 'Normal': 200, 'Rapido' : 100, 'Rapidito': 50, 'MaxJoputa': 10}
speed_var = tk.StringVar(root)
speed_var.set('Normal')
speed_option = tk.OptionMenu(root, speed_var, *speed_dict.keys())
speed_option.grid(row=N, column = 4*N//5, columnspan=N//5, sticky="we")

running = False


root.mainloop()

