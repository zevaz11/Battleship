import tkinter as tk
from PIL import ImageTk, Image

numDestructores = 5


def juegoPrincipal():

    def cambiarNum():
        global numDestructores
        numDestructores = numDestructores-1
        labelDestructor.configure(text=f"Destructor\nDisponibles: {numDestructores}")

    juego = tk.Tk()

    barco1 = Image.open("C:\\Users\\sebas\\OneDrive\\Documents\\TEC\\I Semestre\\Taller\\Proyecto_2\\imagenes\\b1.png")
    barco1 = barco1.resize((50, 50))
    
    destructor = ImageTk.PhotoImage(barco1)

    resolucion=f"{(20+5)*50}x{10*50}+0+0"
    print (resolucion)
    juego.geometry(resolucion)
    juego.configure(background="gray14") 
    juego.resizable(False, False)

    matriz_botones=[[tk.Button(juego) 
                    for c in range(20)] for f in range(10)]

    posx=50*5
    posy=0
    for fila_botones in matriz_botones:
        posx=50*5
        for btn in fila_botones:
            btn.place(x=posx,y=posy)
            btn.configure(height=50, width=50)
            posx+=50 
        posy+=50

    seleccionJugador = tk.Label(juego, text="Jugador 1", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    seleccionJugador.place(x=20, y=20)

    imagen1 = tk.Button(juego, image=destructor, command=lambda:(cambiarNum(), print(numDestructores)))
    imagen1.place(x=20, y=100)
    labelDestructor = tk.Label(juego, text=f"Destructor\nDisponibles: {numDestructores}")
    labelDestructor.place(x=100, y=100)

    juego.mainloop()

juegoPrincipal()