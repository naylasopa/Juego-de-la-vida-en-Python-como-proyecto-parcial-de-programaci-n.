# Juego de la Vida de Conway con Python y Streamlit

# Objetivo del Proyecto
Desarrollar una aplicacion web interactiva del Juego de la Vida de Conway utilizando Python y Streamlit. El objetivo principal es practicar la programacion modular, la simulacion de sistemas y el control de versiones mediante el trabajo colaborativo en GitHub.

# Descripcion del Juego de la Vida
El Juego de la Vida es un automata celular creado por el matematico John Horton Conway. No es un juego tradicional controlado por un jugador, sino que las celulas evolucionan automaticamente en un tablero siguiendo cuatro reglas matematicas basicas:
1. Supervivencia: Una celula viva con dos o tres vecinas vivas sobrevive.
2. Muerte por aislamiento: Una celula viva con menos de dos vecinas vivas muere.
3. Muerte por sobrepoblacion: Una celula viva con mas de tres vecinas vivas muere.
4. Nacimiento: Una celula muerta con exactamente tres vecinas vivas se convierte en una celula viva.

# Integrantes y Responsabilidades
* Nayla (Estudiante A): Logica y reglas del juego (`game_logic.py`). Encargada del conteo de celulas vecinas y el calculo de las generaciones.
* Vanessa (Estudiante B): Visualizacion grafica (`visualization.py`). Encargada de representar el tablero y las calulas en la pantalla.
* Azul (Estudiante C): Interfaz y controles (`app.py`). Encargada de coordinar la aplicacion Streamlit, los botones y los controles.
* Anet / Vexi (Estudiante D): Patrones y pruebas (`patterns.py` y `tests/`). Encargada de los patrones iniciales y las pruebas funcionales.

# Requisitos y Dependencias
* Version de Python: 3.9 o superior.
* Librerias necesarias:La aplicacion requiere las siguientes dependencias (las cuales estan declaradas en el archivo `requirements.txt`):
  * `streamlit`
  * `numpy`
  * `matplotlib`
  * `pytest` (para las pruebas)

# Instrucciones de Instalacion y Ejecucion

1. Clona este repositorio en tu computadora local:
   ``bash
   git clone https://github.com/naylasopa/Juego-de-la-vida-en-Python-como-proyecto-parcial-de-programaci-n..git´´

2. Accede a la carpeta del proyecto e instala las dependencias:
   ``bash
   pip install -r requirements.txt´´

3. Ejecuta la aplicacion con Streamlit
streamlit run app.py

4. La aplicacion se abrira automaticamente en el navegador web

 Descripcion de los Controles
 
La interfaz de usuario cuenta con los siguientes controles:
• Comenzar: Inicia la simulacion automatica de las generaciones.
• Parar: Detiene temporalmente la simulacion sin perder el estado actual.
• Step (Avanzar): Avanza manualmente una sola generacion a la vez.
• Limpiar: Reinicia el tablero dejando todas las celulas muertas.
• Selector de Velocidad: Permite modificar el intervalo de tiempo entre cada generacion (Lento, Normal, Rapido, etc.)

Limitaciones Conocidas y Funciones Implementadas
 
Funciones implementadas:
• Evolucion correcta del automata celular.
• Interfaz web interactiva para manipular el juego.
• Visualizacion grafica con colores distintivos para celulas vivas y muertas.
• Contador de generaciones. 
Limitaciones conocidas:
• El tablero tiene un tamaño fijo establecido en el codigo (por defecto 10x10 o 30x30 segun la configuracion).
• Los limites del tablero son fijos; las celulas de los extremos no se conectan con el lado opuesto.
• La simulacion se reinicia si se recarga la pagina web.


.nn