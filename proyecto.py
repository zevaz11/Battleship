import tkinter as tk
from boardDimensions import *

resultado = []
#Crear el archivo de partidas en caso de no existir
def buscarPartida(nombrePartida:tk.Entry):
    try:
        partidas = open("partidas.txt", "r")
        listaPartidas = [linea.strip() for linea in partidas.readlines()]  #Almacena en una lista, los datos guardados en un archivo de texto, quitando los espacios vacíos.
        partidas.close()
        if nombrePartida in listaPartidas:
            print("Ese nombre de partida ya existe")
        else:
            print("La partida no existe")
    except FileNotFoundError:
        print("La partida no existe")

def crearPartida(partida:tk.Entry,jugador1:tk.Entry, jugador2:tk.Entry, numColumnas:tk.Entry, numFilas:tk.Entry):
    global resultado
    partidaTemporal = partida.get()
    #Crear el archivo de partidas en caso de no existir
    try:
        partidas = open("partidas.txt", "r")
        listaPartidas = [linea.strip() for linea in partidas.readlines()]

        if partidaTemporal in listaPartidas:
            print("Ese nombre de partida ya existe")
        else:
            validarDimensiones = dimensionsEntries(numColumnas,numFilas)
            if validarDimensiones == True:
                partidasTotales = open("partidas.txt", "a")
                partidasTotales.write(f"\n{partidaTemporal}")
                partidasTotales.close()   

                resultado.append(partida.get())
                resultado.append(jugador1.get())
                resultado.append(jugador2.get())
                resultado.append(numColumnas.get())

                partidaNueva = open(f"{partidaTemporal}.txt","w")
                partidaNueva.write(f"{resultado[1]}")
                for dato in resultado[2:]:
                    partidaNueva.write(f"\n{dato}")
                partidaNueva.close()

                resultado.clear()
            else:
                pass

    except FileNotFoundError:
        partidas = open("partidas.txt","w")
        partidas.write(f"{partidaTemporal}")
        partidas.close()

def cargarPartida():
    """Abre una ventana que contiene las partidas guardadas
    """
    #Ventana de cargar partida
    partidasGuardadas = tk.Tk()
    partidasGuardadas.title("Partidas guardadas")
    partidasGuardadas.geometry("1000x700")
    partidasGuardadas.configure(background="gray14")
    partidasGuardadas.resizable(False, False)
    #Título
    tituloRegistro = tk.Label(partidasGuardadas, text="Cargar Partida", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.2, anchor = "center")
    #Ingresar los datos
    ingresarPartida = tk.Label(partidasGuardadas, text="Ingrese el nombre de la partida:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    ingresarPartida.place(relx=0.15,rely=0.45)
    partidaCargada = tk.Entry(partidasGuardadas, background="gray25", fg="snow", font=('Helvetica bold', 20))
    partidaCargada.place(relx=0.55, rely=0.45)
    botonIngresar = tk.Button(partidasGuardadas, text="Ingresar", command = lambda:(buscarPartida(partidaCargada)))
    botonIngresar.place(relx=0.5, rely=0.65, anchor = "center", height=50, width=200)

    partidasGuardadas.mainloop()

def nuevaPartida():
    """Abre una ventana llamada nueva partida
    """
    #Ventana de nueva partida
    partidaNueva = tk.Tk()
    partidaNueva.title("Nueva Partida")
    partidaNueva.geometry("1000x700")
    partidaNueva.configure(background="gray14")  #Fondo del menú de color gris
    partidaNueva.resizable(False, False)
    #Título de la ventana
    tituloRegistro = tk.Label(partidaNueva, text="Crear Partida", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.15, anchor = "center")
    #Etiquetas
    labelNombrePartida = tk.Label(partidaNueva, text="Nombre de la partida:", background="gray14", fg= "cyan", font=('Helvetica bold', 20))
    labelJugador1 = tk.Label(partidaNueva, text="Jugador #1:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelJugador2 = tk.Label(partidaNueva, text="Jugador #2:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelColumnas = tk.Label(partidaNueva, text="Columnas:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelFilas = tk.Label(partidaNueva, text="Filas:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    #Espacios de entrada
    nombrePartida = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador1 = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador2 = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    columnas = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    filas = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    #Colocación de las etiquetas
    labelNombrePartida.place(relx=0.2, rely=0.25)
    labelJugador1.place(relx=0.2, rely=0.35)
    labelJugador2.place(relx=0.2, rely=0.45)
    labelColumnas.place(relx=0.2, rely=0.55)
    labelFilas.place(relx=0.2, rely=0.65)
    #Colocación de las entradas
    nombrePartida.place(relx=0.48, rely=0.25)
    jugador1.place(relx=0.36, rely=0.35)
    jugador2.place(relx=0.36, rely=0.45)
    columnas.place(relx=0.35, rely=0.55)
    filas.place(relx=0.285, rely=0.65)

    #Botón para ingresar los datos escritos
    registrarJugador = tk.Button(partidaNueva, text="Empezar partida", command=lambda:(crearPartida(nombrePartida, jugador1, jugador2, columnas, filas)))
    registrarJugador.place(relx=0.5, rely=0.82, anchor = "center", height=50, width=200)

    partidaNueva.mainloop()

def menuJuego():
    """Menú principal del juego Battleship
    """
    juego = tk.Tk()
    juego.title("Battleship")
    juego.geometry("1000x700")
    juego.configure(background="gray14")  #Fondo del menú de color gris
    juego.resizable(False, False)  #Evitar que la pantalla sea reajustable
    
    #Título del juego
    tituloJuego = tk.Label(juego, text="BATTLESHIP", background="gray14", fg="cyan", font=('Helvetica bold', 50))
    tituloJuego.place(relx=0.5, rely=0.2, anchor = "center")

    #Botón de partida nueva
    botonPartidaN = tk.Button(juego, text="Nueva Partida", command=lambda:(juego.destroy(), nuevaPartida()))
    botonPartidaN.place(relx=0.5, rely=0.4, anchor = "center", height=50, width=200)

    #Botón de cargar partida
    botonCargarP = tk.Button(juego, text="Cargar partida", command=lambda:(juego.destroy(),cargarPartida()))
    botonCargarP.place(relx=0.5, rely=0.5, anchor = "center", height=50, width=200)

    #Botón de salir
    botonSalir = tk.Button(juego, text="Salir del juego", command = juego.destroy)
    botonSalir.place(relx=0.5, rely=0.6, anchor = "center", height=50, width=200)

    #Nueva partida
    #Cargar partida

    juego.mainloop()

menuJuego()

#Referencias
#https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#https://www.geeksforgeeks.org/python-tkinter-text-widget/
#command=lambda:(juego.destroy(),nuevaPartida())

#Themes
#Bearded Theme Void / Metallian