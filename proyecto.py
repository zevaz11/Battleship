import tkinter as tk
from PIL import ImageTk, Image

def registroMenu():
    """Abre una ventana llamada registro de jugadores
    """
    registro = tk.Tk()
    registro.title("Registro de jugadores")
    registro.geometry("1000x700")
    registro.configure(background="gray14")  #Fondo del menú de color gris
    registro.resizable(False, False)

    tituloRegistro = tk.Label(registro, text="Registro de jugadores", background="gray14", fg="yellow2")
    tituloRegistro.config(font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.2, anchor = "center")

    registrar = tk.Text(registro)

    registro.mainloop()

def menuJuego():
    """Menú principal del juego Battleship
    """
    juego = tk.Tk()
    juego.title("Battleship")
    juego.geometry("1000x700")
    juego.configure(background="gray14")  #Fondo del menú de color gris
    juego.resizable(False, False)  #Evitar que la pantalla sea reajustable
    
    #Título del juego
    tituloJuego = tk.Label(juego, text="BATTLESHIP", background="gray14", fg="cyan")
    tituloJuego.config(font=('Helvetica bold', 50))
    tituloJuego.place(relx=0.5, rely=0.2, anchor = "center")

    #Botón de partida nueva
    nuevaPartida = tk.Button(juego, text="Nueva Partida")
    nuevaPartida.place(relx=0.5, rely=0.4, anchor = "center", height=50, width=200)

    #Botón de cargar partida
    cargarPartida = tk.Button(juego, text="Cargar partida")
    cargarPartida.place(relx=0.5, rely=0.5, anchor = "center", height=50, width=200)

    #Botón para entrar al registro de jugadores
    botonRegistro = tk.Button(juego, text="Registro de jugadores", command=lambda:(juego.destroy(),registroMenu()))
    botonRegistro.place(relx=0.5, rely=0.6, anchor = "center", height=50, width=200)

    #Botón de salir
    botonSalir = tk.Button(juego, text="Salir del juego", command = juego.destroy)
    botonSalir.place(relx=0.5, rely=0.7, anchor = "center", height=50, width=200)

    #Nueva partida
    #Cargar partida

    juego.mainloop()

menuJuego()





#Referencias
#https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#https://www.geeksforgeeks.org/python-tkinter-text-widget/

#Themes
#Bearded Theme Void / Metallian