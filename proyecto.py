from tkinter import *
from boardDimensions import *
resultado = [] #almacena temporalmente los datos de partida
#Crear el archivo de partidas en caso de no existir
def cargarPartida():
    """Abre una ventana que contiene las partidas guardadas
    """

    def buscarPartida(nombrePartida:Entry):
        try:
            partidas = open("partidas.txt", "r")
            listaPartidas = [linea.strip() for linea in partidas.readlines()]  #Almacena en una lista, los datos guardados en un archivo de texto, quitando los espacios vacíos.
            partidas.close()
            if nombrePartida in listaPartidas:
                partida = open(f"{nombrePartida}.txt", "r")
                partidaCargada = [datos.strip() for datos in partida.readlines()]
            else:
                print("La partida no existe")
        except FileNotFoundError:
            print("La partida no existe")
            
    #Ventana de cargar partida
    partidasGuardadas = Tk()
    partidasGuardadas.title("Partidas guardadas")
    partidasGuardadas.geometry("1000x700")
    partidasGuardadas.configure(background="gray14")
    partidasGuardadas.resizable(False, False)
    #Título
    tituloRegistro = Label(partidasGuardadas, text="Cargar Partida", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.2, anchor = "center")
    #Ingresar los datos
    ingresarPartida = Label(partidasGuardadas, text="Ingrese el nombre de la partida:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    ingresarPartida.place(relx=0.15,rely=0.45)
    partidaCargada = Entry(partidasGuardadas, background="gray25", fg="snow", font=('Helvetica bold', 20))
    partidaCargada.place(relx=0.55, rely=0.45)
    botonIngresar = Button(partidasGuardadas, text="Ingresar", command = lambda:(buscarPartida(partidaCargada,)))
    botonIngresar.place(relx=0.5, rely=0.65, anchor = "center", height=50, width=200)

    partidasGuardadas.mainloop()

def nuevaPartida():
    """Abre una ventana llamada nueva partida
    """
    nicknames = []
    def registrarNicknames ():
        entryNicknameJ1 = entryNickJ1.get()
        entryNicknameJ2 = entryNickJ2.get()
        if entryNicknameJ1 == entryNicknameJ2: 
            messagebox.showerror("Error", "Los jugadores no pueden tener nicknames iguales")
        else:
            nicknames.append (entryNicknameJ1) # Agrega los nicknames escritos en el entry a la lista de nicknames
            nicknames.append (entryNicknameJ2) 
            messagebox.showinfo("Info", "Nicknames registrados")
            messagebox.showinfo("Info",nicknames)
            crearPartida(nombrePartida, jugador1, jugador2), dimensionsEntries()
    def crearPartida(partida:Entry,jugador1:Entry, jugador2:Entry):
        global resultado
        nonlocal menuPartidaNueva
        partidaTemporal = partida.get()
        #Crear el archivo de partidas en caso de no existir
        try:
            partidas = open("partidas.txt", "r")
            listaPartidas = [linea.strip() for linea in partidas.readlines()]    
            partidas.close()
        except FileNotFoundError:
            partidas = open("partidas.txt","w")
            partidas.close()
            partidas = open("partidas.txt", "r")
            listaPartidas = [linea.strip() for linea in partidas.readlines()]    
            partidas.close()

        if partidaTemporal in listaPartidas:
                print("Ese nombre de partida ya existe")
        else:
            partidasTotales = open("partidas.txt", "a")
            partidasTotales.write(f"\n{partidaTemporal}")
            partidasTotales.close()   
            resultado.append(partida.get())
            resultado.append(jugador1.get())
            resultado.append(jugador2.get())
            resultado.append(nicknames)
            partidaNueva = open(f"{partidaTemporal}.txt","w")
            partidaNueva.write(f"{resultado[1]}")
            for dato in resultado[2:]:
                partidaNueva.write(f"\n{dato}")
            partidaNueva.close()
            
            menuPartidaNueva.destroy()
            resultado.clear()

    #Ventana de nueva partida
    menuPartidaNueva = Tk()
    menuPartidaNueva.title("Nueva Partida")
    menuPartidaNueva.geometry("1000x700")
    menuPartidaNueva.configure(background="gray14")  #Fondo del menú de color gris
    menuPartidaNueva.resizable(False, False)
    #Título de la ventana
    tituloRegistro = Label(menuPartidaNueva, text="Crear Partida", background="gray14", fg="yellow2", font=('Helvetica bold', 35))
    tituloRegistro.place(relx=0.5, rely=0.15, anchor = "center")
    #Etiquetas
    labelNombrePartida = Label(menuPartidaNueva, text="Nombre de la partida:", background="gray14", fg= "cyan", font=('Helvetica bold', 20))
    labelJugador1 = Label(menuPartidaNueva, text="Jugador #1:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelJugador2 = Label(menuPartidaNueva, text="Jugador #2:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelNick1 = Label(menuPartidaNueva, text="Nickname #1:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    labelNick2 = Label(menuPartidaNueva, text="Nickname #2:", background="gray14", fg="cyan", font=('Helvetica bold', 20))
    #Espacios de entrada
    nombrePartida = Entry(menuPartidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador1 = Entry(menuPartidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    jugador2 = Entry(menuPartidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    entryNickJ1 = Entry (menuPartidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))
    entryNickJ2 = Entry (menuPartidaNueva, background="gray25", fg="snow", font=('Helvetica bold', 20))

    #Colocación de las etiquetas
    labelNombrePartida.place(relx=0.2, rely=0.25)
    labelJugador1.place(relx=0.2, rely=0.35)
    labelJugador2.place(relx=0.2, rely=0.45)
    labelNick1.place(relx=0.2, rely=0.55)
    labelNick2.place(relx=0.2, rely=0.65)
    #Colocación de las entradas
    nombrePartida.place(relx=0.48, rely=0.25)
    jugador1.place(relx=0.36, rely=0.35)
    jugador2.place(relx=0.36, rely=0.45)
    entryNickJ1.place (relx=0.40,rely=0.55)
    entryNickJ2.place (relx=0.40,rely=0.65)

    #Botón para ingresar los datos escritos
    registrarJugador = Button(menuPartidaNueva, text="Empezar partida", command=lambda: (registrarNicknames()))
    registrarJugador.place(relx=0.5, rely=0.82, anchor = "center", height=50, width=200)

    menuPartidaNueva.mainloop()

#Referencias
#https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#https://www.geeksforgeeks.org/python-tkinter-text-widget/
#command=lambda:(juego.destroy(),nuevaPartida())

#Themes
#Bearded Theme Void / Metallian