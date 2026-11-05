import numpy as np #utilizar/importar desde la librería numpy, vamos a utilizar matrices de dos dimenciones 
#agregamos tres variables
N = 10 #dimensiones de nuetra matriz, tienen que ser cyadraadas
ON = 1 #celda viva/true/si/1
OFF = 0 #celda muerta/false/no/0
#crear el grid(es la matriz donde van a estar todos los cuadritos)
grid = np.full((N,N), OFF)
#definición de la función update, que va a actualizar el grid, es decir, va a cambiar el estado de las celdas dependiendo de las reglas del juego de la vida
def update(grid):
    newGrid = grid.copy() #reamos una copuia del grid
    for i in range(N): #acceder a los elementos de la matriz
        for j in range(N):
             #crear una variable que nos diga cuantas celda svivas hay/ acceder al grid para ver 8 veces quien esta viva
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + #agregar el modulo N para hacer el efecto wraparround
                    grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                    grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                    grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            #escribir las reglas
            if grid[i,j] == ON: #Si las celdas están prendidas:
                if (total<2) or (total>3): #si el total es menor que dos ó el total es mayor que 3(reglas) se mueren las celdas
                    newGrid[i,j] = OFF
            else:
                if total == 3: #si la celula esta muerta: 
                    newGrid[i,j] = ON #vamos a revivirlas
    #logica del juego de la vida            
    return newGrid
