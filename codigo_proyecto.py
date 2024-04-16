import tkinter as tk
from PIL import ImageTk, Image

numDestructores = 6
numCruceros = 4


def juegoPrincipal():

    casillasJugador1 = []

    def girarImagen():
        barco1.rotate(0)
        destructorImg = ImageTk.PhotoImage(barco1)
        destructor.configure(image=destructorImg)


    def accion(x,y):
        """Toma la posición del botón pulsado y lo configura de acuerdo a esto

        Args:
            x (_type_): el número de columna del botón
            y (_type_): el número de fila del botón
        """
        global numDestructores

        if [x,y] in casillasJugador1:  #Esto para que no haya barcos en la misma casilla
            numDestructores +=1  #Suma 1 a el número de destructores disponible para que no suba ni baje su cantidad
        else:
            print (f"x={x},y={y}")
            casillas[y][x].configure(image=destructorImg)  #Añade la imagen del barco destructor al botón  
            casillasJugador1.append([x,y])  #Guarda la coordenada del botón en la lista con todas las coordenas del jugador 1

        if len(casillasJugador1) == 6:
            destructor.destroy()
            labelDestructor.destroy()  
            #Se posiciona la imagen del crucero porque ya se colocaron todos los destructores
            crucero21.place(x=20, y=100)
            labelCrucero21.place(x=100, y=100)
            crucero22.place(x=20, y=200)
            labelCrucero22.place(x=100, y=200)
        print(casillasJugador1)

    def desactivarCasillas():
        for fila_botones in casillas:
            for btn in fila_botones:
                btn.configure(state=tk.DISABLED)
    
    def activarCasillas():
        for filaBotones in casillas:
            for btn in filaBotones:
                btn.configure(state=tk.NORMAL) 

    def cambiarNum():

        global numDestructores

        numDestructores = numDestructores-1
        labelDestructor.configure(text=f"Destructor\nDisponibles: {numDestructores}")
            

    juego = tk.Tk()


    #Ajustes de la ventana del jugador 1
    resolucion=f"{(20+5)*50}x{10*50}+0+0"
    print (resolucion)
    juego.geometry(resolucion)
    juego.configure(background="gray14") 
    juego.resizable(False, False)

    seleccionJugador = tk.Label(juego, text="Jugador 1", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    seleccionJugador.place(x=20, y=20)

    #Creación de la matriz del jugador 1 
    casillas=[[tk.Button(juego, command=lambda x=c,y=f:(accion(x,y), desactivarCasillas())) 
                    for c in range(20)] for f in range(10)]

    posx=50*5
    posy=0
    for fila_botones in casillas:
        posx=50*5
        for btn in fila_botones:
            btn.place(x=posx,y=posy)
            btn.configure(state=tk.DISABLED, height=50, width=50)
            posx+=50 
        posy+=50

    #Imágenes de los barcos
    barco1 = Image.open("C:\\Users\\sebas\\OneDrive\\Documents\\TEC\\I Semestre\\Taller\\Proyecto_2\\imagenes\\b1.png")
    barco1 = barco1.resize((50, 50))
    destructorImg = ImageTk.PhotoImage(barco1)

    barco21 = Image.open("C:\\Users\\sebas\\OneDrive\\Documents\\TEC\\I Semestre\\Taller\\Proyecto_2\\imagenes\\b21.png")
    barco22 = Image.open("C:\\Users\\sebas\\OneDrive\\Documents\\TEC\\I Semestre\\Taller\\Proyecto_2\\imagenes\\b22.png")
    barco21 = barco21.resize((50,50))
    barco22 = barco22.resize((50,50))
    crucero21Img = ImageTk.PhotoImage(barco21)
    crucero22Img = ImageTk.PhotoImage(barco22)

    #Posicionamiento de los barcos
    destructor = tk.Button(juego, image=destructorImg, command=lambda:(cambiarNum(), activarCasillas(), print(numDestructores)))
    destructor.place(x=20, y=100)
    labelDestructor = tk.Label(juego, text=f"Destructor\nDisponibles: {numDestructores}", background="gray14", fg="snow")
    labelDestructor.place(x=100, y=100)

    crucero21 = tk.Button(juego, image=crucero21Img)
    labelCrucero21 = tk.Label(juego, text=f"Crucero\n(Parte delantera)\nDisponibles: {numCruceros}", background="gray14", fg="snow")

    crucero22 = tk.Button(juego, image=crucero22Img)
    labelCrucero22 = tk.Label(juego, text=f"Crucero\n(Parte trasera)\nDisponibles: {numCruceros}", background="gray14", fg="snow")

    girar = tk.Button(juego, text="Girar", command=girarImagen)
    girar.place(x=50, y=300)
    juego.mainloop()

juegoPrincipal()