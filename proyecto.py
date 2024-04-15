import tkinter as tk
from PIL import ImageTk, Image

def nuevaPartida():
    """Abre una ventana llamada nueva partida
    """
    partidaNueva = tk.Tk()
    partidaNueva.title("Nueva Partida")
    partidaNueva.geometry("1000x700")
    partidaNueva.configure(background="gray14")  #Fondo del menú de color gris
    partidaNueva.resizable(False, False)

    tituloRegistro = tk.Label(partidaNueva, text="Menú de partida nueva", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.2, anchor = "center")

    labelNombrePartida = tk.Label(partidaNueva, text="Nombre de la partida:", background="gray14", fg= "cyan", font=('Helvetica bold', 20))
    labelJugador1 = tk.Label(partidaNueva, text="Jugador #1:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelJugador2 = tk.Label(partidaNueva, text="Jugador #2:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelDimensiones = tk.Label(partidaNueva, text="Dimensiones:", background="gray14", fg="cyan", font=('Helvetica bold', 20))

    nombrePartida = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador1 = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador2 = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    dimensiones = tk.Entry(partidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))

    labelNombrePartida.place(relx=0.2, rely=0.35)
    labelJugador1.place(relx=0.2, rely=0.45)
    labelJugador2.place(relx=0.2, rely=0.55)
    labelDimensiones.place(relx=0.2, rely=0.65)

    nombrePartida.place(relx=0.48, rely=0.35)
    jugador1.place(relx=0.36, rely=0.45)
    jugador2.place(relx=0.36, rely=0.55)
    dimensiones.place(relx=0.385, rely=0.65)

    #Botón para ingresar los datos escritos
    registrarJugador = tk.Button(partidaNueva, text="Empezar partida")
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
    cargarPartida = tk.Button(juego, text="Cargar partida")
    cargarPartida.place(relx=0.5, rely=0.5, anchor = "center", height=50, width=200)

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