from tkinter import *
from tkinter import messagebox
def boardColumns ():
  """ La función boardColumns, se encarga de obtener el valor ingresado para el numero de columnas y lo reasigna a otra variable para que pueda ser obtenido desde el archivo principal
  Returns:
      scaleX: el numero de columnas del tablero
  """  
  scaleX = valueX
  return scaleX

def boardRows ():
  """ La función boardRows, se encarga de obtener el valor ingresado para el numero de filas y lo reasigna a otra variable para que pueda ser obtenido desde el archivo principal
  Returns:
      scaleY: el numero de filas del tablero
  """
  scaleY = valueY
  return scaleY

def dimensionsEntries():
  """ La funcion DimensionsEntries, almacena y ejecuta el codigo necesario para mostrar los inputs con el tamaño del tablero
  """
  def checkEntry(text):
    """ La función CheckEntry, revisa que el texto escrito en los inputs sean caracteres validos.
    Args:
        text (Entry): texto ingresado en los inputs
    Returns:
        bool: devuelve un falso en caso de que se escriba un dato no valido
    """
    if text.isdigit() or text == "":
        return True
    else:
        messagebox.showerror("Error", "Solo se pueden colocar numeros enteros")
        return False

  def checkValues():
    """ La función checkValues, revisa los datos ingresados y se asegura de que cumplan con todos los requisitos
    """
    intX = entryX.get()
    intY = entryY.get()
    if intX == "" or intY == "": #Revisa si alguno de los campos está vacio
      messagebox.showerror("Error", "Uno de los campos está vacio.")

    else:
      global valueX
      global valueY
      valueX = int(intX)
      valueY = int(intY)
      if valueX < 20: #revisa que el valor de las columnas no sea menor a 20
        messagebox.showerror("Error", "El numero de columnas no puede ser menor a 20")
      elif valueY < 10: #revisa que el valor de las filas no sea menor a 10
        messagebox.showerror("Error", "El numero de filas no puede ser menor a 10")
      elif valueX % 2 != 0: #revisa que el valor de las columnas no sea impar
        messagebox.showerror("Error", "El numero de columnas no puede ser impar")
      elif valueY % 2 != 0: #revisa que el valor de las filas no sea impar
        messagebox.showerror("Error", "El numero de filas no puede ser impar")
      else:
        messagebox.showinfo("Dimensiones", f"Las columnas miden {valueX} y las filas miden {valueY}")
        inputWindow.destroy()

  ##Ventana para el ingreso de los datos##
  inputWindow = Tk()
  inputWindow.title("Board Dimensions")

  #Entry para las columnas
  checked = inputWindow.register(checkEntry)
  entryX = Entry(inputWindow, width="50", validate="key", validatecommand=(checked, "%P"))
  entryX.pack(pady=10)

  #Entry para las filas
  checked = inputWindow.register(checkEntry)
  entryY = Entry(inputWindow, width="50", validate="key", validatecommand=(checked, "%P"))
  entryY.pack(pady=10)

  #Boton para comprobar los valores.
  continueButton = Button(inputWindow, text="Continuar", command=checkValues )
  continueButton.pack(padx=5,pady=5)

  inputWindow.mainloop()

dimensionsEntries()
boardColumns()
boardRows()