import tkinter as tk

def tablero2(x: int, y: int) -> tk.Tk:
    juego = tk.Tk()
    juego.title("Battleship")

    # Obtener el ancho y alto de la pantalla
    screen_width = juego.winfo_screenwidth()
    screen_height = juego.winfo_screenheight()

    # Calcula el tamaño de la ventana
    ventana_ancho = (x+5) * 35
    ventana_alto = y * 50

    # Establece el tamaño de la ventana
    resolucion = f"{ventana_ancho}x{ventana_alto}+0+0"
    juego.geometry(resolucion)
    matriz_botones = [[tk.Button(juego) for _ in range(x)] for _ in range(y)]
    for fila, fila_botones in enumerate(matriz_botones):
        for columna, btn in enumerate(fila_botones):
            btn.place(x=columna * 50, y=fila * 50, width=50, height=50)

    juego.mainloop()
    return juego

tablero2(20, 12)