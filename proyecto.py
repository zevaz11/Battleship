import tkinter as tk
from PIL import ImageTk, Image

def menuJuego():
    juego = tk.Tk()
    juego.title("Battleship")
    juego.geometry("1000x700")
    juego.configure(background="gray14")  #Fondo del menú de color gris
    juego.resizable(False, False)  #Evitar que la pantalla sea reajustable

    tituloJuego = tk.Label(juego, text="Battleship", background="gray14", fg="cyan")
    
    #tituloJuego.grid(row=1, column=3)
    tituloJuego.config(font=('Helvetica bold', 50))

    tituloJuego.place(relx=0.5, rely=0.2, anchor = "center")

    boton1 = tk.Button(juego, text="hola")
    boton1.place(x=350, y=350, height=50, width=50)

    #Menú
    #Nueva partida
    #Cargar partida

    juego.mainloop()