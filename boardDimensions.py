import sys
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
def boardColumns ():
  """ La función boardColumns, se encarga de generar y mostrar un input para que el usuario defina el numero de columnas del tablero
  Returns:
      int: el numero de columnas del tablero
  """  
  scaleX = int(simpledialog.askstring("Columnas", "Introduce la cantidad de columnas:"))
  if scaleX < 20: #advertirle al usuario de que el numero de colunmas no puede ser menor a 20
    messagebox.showinfo("Advertencia", "El numero de columnas no puede ser menor a 20")
    sys.exit() # Esto es provisional, el código final no tiene que cerrarse si se le da un dato erroneo, en su lugar tendría que volver a abrir el input.
  elif scaleX % 2 != 0: #advertirle al usuario de que el numero de columnas no puede ser impar
    messagebox.showinfo("Advertencia", "El numero de columnas no puede ser impar")
    sys.exit()
  return scaleX

def boardRows ():
  """ La función boardRows, se encarga de generar y mostrar un input para que el usuario defina el numero de filas del tablero
  Returns:
      int: el numero de filas del tablero
  """
  scaleY = int(simpledialog.askstring("Filas", "Introduce la cantidad de filas:"))
  if scaleY < 10: #advertirle al usuario de que el numero de filas no puede ser menor a 10
    messagebox.showinfo("Advertencia", "El numero de filas no puede ser menor a 10")
    sys.exit() # // quitar despues
  elif scaleY % 2 != 0: #advertirle al usuario de que el numero de filas no puede ser impar
    messagebox.showinfo("Advertencia", "El numero de filas no puede ser impar")
    sys.exit() # // quitar despues
  return scaleY