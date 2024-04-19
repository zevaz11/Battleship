from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

buttonsMatrixPlayer1= []
buttonsMatrixPlayer2= []
shipCount = []
rotate = 0
##Diccionarios con la información de los barcos##
currentShipIndex1 = 0
currentShipIndex2 = 0
shipsPlayer1 = {
  "ship1" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship2" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship3" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship4" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship5" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship6" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship7" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship8" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship9" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship10": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship11": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship12": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""}
}
shipsPlayer2 = {
  "ship1" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship2" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship3" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship4" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship5" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship6" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship7" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship8" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship9" : {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship10": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship11": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""},
  "ship12": {"visibility": True, "movibility": True, "alive": True, "type": "", "direction": "", "position":[], "image": ""}
}
#Llaves de las listas#
shipKeys1 = list(shipsPlayer1.keys())
shipKeys2 = list(shipsPlayer2.keys())

##Variables de los barcos##
shipType = 1 #maneja el tipo de nave
def shipsImages ():
  global destructorRight, destructorUp, destructorLeft, destructorDown
  global cruceroRight, cruceroRight2, cruceroUp, cruceroUp2, cruceroLeft, cruceroLeft2, cruceroDown, cruceroDown2
  global acorazadoRight, acorazadoRight2, acorazadoRight3, acorazadoUp, acorazadoUp2, acorazadoUp3, acorazadoLeft, acorazadoLeft2, acorazadoLeft3, acorazadoDown, acorazadoDown2, acorazadoDown3
  global keyQ, keyW, keyE # Boleanos para los inputs de las letras Q, W y E
  #destructor
  destructorRight = Image.open("b1.png")
  destructorRight = destructorRight.resize((50,50))
  destructorUp = destructorRight.rotate(90)
  destructorUp = destructorUp.resize((50,50))
  destructorLeft = destructorRight.rotate(180)
  destructorLeft = destructorLeft.resize((50,50))
  destructorDown = destructorRight.rotate(270)
  destructorDown = destructorDown.resize((50,50))
  #
  destructorRight = ImageTk.PhotoImage(destructorRight)
  destructorUp = ImageTk.PhotoImage(destructorUp)
  destructorLeft = ImageTk.PhotoImage(destructorLeft)
  destructorDown = ImageTk.PhotoImage(destructorDown)
  #crucero
  cruceroRight = Image.open("b22.png")
  cruceroRight2 = Image.open("b21.png")
  cruceroRight = cruceroRight.resize((50,50))
  cruceroRight2 = cruceroRight2.resize((50,50))
  #
  cruceroUp = cruceroRight.resize((50,50))
  cruceroUp = cruceroUp.rotate(90)
  cruceroUp2 = cruceroRight2.resize((50,50))
  cruceroUp2 = cruceroUp2.rotate(90)
  #
  cruceroLeft = cruceroRight.resize((50,50))
  cruceroLeft = cruceroLeft.rotate(180)
  cruceroLeft2 = cruceroRight2.resize((50,50))
  cruceroLeft2 = cruceroLeft2.rotate(180)
  #
  cruceroDown = cruceroRight.resize((50,50))
  cruceroDown = cruceroDown.rotate(270)
  cruceroDown2 = cruceroRight2.resize((50,50))
  cruceroDown2 = cruceroDown2.rotate(270)
  #
  cruceroRight = ImageTk.PhotoImage(cruceroRight)
  cruceroRight2 = ImageTk.PhotoImage(cruceroRight2)
  cruceroUp = ImageTk.PhotoImage(cruceroUp)
  cruceroUp2 = ImageTk.PhotoImage(cruceroUp2)
  cruceroLeft = ImageTk.PhotoImage(cruceroLeft)
  cruceroLeft2 = ImageTk.PhotoImage(cruceroLeft2)
  cruceroDown = ImageTk.PhotoImage(cruceroDown)
  cruceroDown2 = ImageTk.PhotoImage(cruceroDown2)
  #acorazado
  acorazadoRight = Image.open("b33.png")
  acorazadoRight2 = Image.open("b32.png")
  acorazadoRight3 = Image.open("b31.png")
  acorazadoRight = acorazadoRight.resize((50,50))
  acorazadoRight2 = acorazadoRight2.resize((50,50))
  acorazadoRight3 = acorazadoRight3.resize((50,50))
  #
  acorazadoUp = acorazadoRight.resize((50,50))
  acorazadoUp = acorazadoUp.rotate(90)
  acorazadoUp2 = acorazadoRight2.resize((50,50))
  acorazadoUp2 = acorazadoUp.rotate(90)
  acorazadoUp3 = acorazadoRight3.resize((50,50))
  acorazadoUp3 = acorazadoUp.rotate(90)
  #
  acorazadoLeft = acorazadoRight.resize((50,50))
  acorazadoLeft = acorazadoLeft.rotate(180)
  acorazadoLeft2 = acorazadoRight2.resize((50,50))
  acorazadoLeft2 = acorazadoLeft.rotate(180)
  acorazadoLeft3 = acorazadoRight3.resize((50,50))
  acorazadoLeft3 = acorazadoLeft.rotate(180)
  #
  acorazadoDown = acorazadoRight.resize((50,50))
  acorazadoDown = acorazadoDown.rotate(270)
  acorazadoDown2 = acorazadoRight2.resize((50,50))
  acorazadoDown2 = acorazadoDown.rotate(270)
  acorazadoDown3 = acorazadoRight3.resize((50,50))
  acorazadoDown3 = acorazadoDown.rotate(270)
  #
  acorazadoRight = ImageTk.PhotoImage(acorazadoRight)
  acorazadoRight2= ImageTk.PhotoImage(acorazadoRight2)
  acorazadoRight2= ImageTk.PhotoImage(acorazadoRight3)
  acorazadoUp = ImageTk.PhotoImage(acorazadoUp)
  acorazadoUp2 = ImageTk.PhotoImage(acorazadoUp2)
  acorazadoUp2 = ImageTk.PhotoImage(acorazadoUp3)
  acorazadoLeft = ImageTk.PhotoImage(acorazadoLeft)
  acorazadoLeft2 = ImageTk.PhotoImage(acorazadoLeft2)
  acorazadoLeft2 = ImageTk.PhotoImage(acorazadoLeft3)
  acorazadoDown = ImageTk.PhotoImage(acorazadoDown)
  acorazadoDown2 = ImageTk.PhotoImage(acorazadoDown2)
  acorazadoDown2 = ImageTk.PhotoImage(acorazadoDown3)
  
def onClickTrue(): # Permite que la Q, W y E puedan volver a ser usadas para seleccionar otro barco, pero solo despues de que el barco anterior sea colocado.
  global  keyQ, keyW, keyE
  keyQ = keyW = keyE = True 
def onClickFalse(): # Desactiva las teclas Q, W y R para que no puedan volver a ser usadas hasta que se coloque el barco seleccionado
  global  keyQ, keyW, keyE
  keyQ = keyW = keyE = False

##Funciones KeyBinds##
def rotateShip(event):
  global rotate
  rotate += 1
  if rotate > 3:
    rotate = 0

def selectShip1(event):
  global destructorRight, destructorUp, destructorLeft, destructorDown #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global keyQ
  if currentShipIndex1 > len(shipsPlayer1):
    messagebox.showinfo("Advertencia","Ya no quedan mas naves por colocar")
  elif keyQ == True:
    currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
    if rotate == 0:
      shipsPlayer1[currentShipKey]['image'] = destructorRight
      shipsPlayer1[currentShipKey]['direction'] = "Right"
    elif rotate == 1:
      shipsPlayer1[currentShipKey]['image'] = destructorUp
      shipsPlayer1[currentShipKey]['direction'] = "Up"
    elif rotate == 2:
      shipsPlayer1[currentShipKey]['image'] = destructorLeft
      shipsPlayer1[currentShipKey]['direction'] = "Left"
    elif rotate == 3:
      shipsPlayer1[currentShipKey]['image'] = destructorDown
      shipsPlayer1[currentShipKey]['direction'] = "Down"
    shipType = 1
    shipsPlayer1[currentShipKey]['type'] = "Destructor"
    messagebox.showinfo("Data",shipsPlayer1) #//Solo para pruebas, quitar al final
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def selectShip2(event):
  global cruceroRight, cruceroRight2, cruceroUp, cruceroUp2, cruceroLeft, cruceroLeft2, cruceroDown, cruceroDown2 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global keyW
  if currentShipIndex1 > len(shipsPlayer1):
    messagebox.showinfo("Advertencia","Ya no quedan mas naves por colocar")
  elif keyW == True:
    currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
    if rotate == 0:
      shipsPlayer1[currentShipKey]['image'] = cruceroRight
      shipsPlayer1[currentShipKey]['direction'] = "Right"
    elif rotate == 1:
      shipsPlayer1[currentShipKey]['image'] = cruceroUp
      shipsPlayer1[currentShipKey]['direction'] = "Up"
    elif rotate == 2:
      shipsPlayer1[currentShipKey]['image'] = cruceroLeft
      shipsPlayer1[currentShipKey]['direction'] = "Left"
    elif rotate == 3:
      shipsPlayer1[currentShipKey]['image'] = cruceroDown
      shipsPlayer1[currentShipKey]['direction'] = "Down"
    shipType = 2
    shipsPlayer1[currentShipKey]['type'] = "Crucero"
    messagebox.showinfo("Data",shipsPlayer1) #//Solo para pruebas, quitar al final
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def selectShip3(event):
  global acorazadoRight, acorazadoRight2, acorazadoRight3, acorazadoUp, acorazadoUp2, acorazadoUp3, acorazadoLeft, acorazadoLeft2, acorazadoLeft3, acorazadoDown, acorazadoDown2, acorazadoDown3 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global keyE
  if currentShipIndex1 > len(shipsPlayer1):
    messagebox.showinfo("Advertencia","Ya no quedan mas naves por colocar")
  elif keyE == True:
    currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
    if rotate == 0:
      shipsPlayer1[currentShipKey]['image'] = acorazadoRight
      shipsPlayer1[currentShipKey]['direction'] = "Right"
    elif rotate == 1:
      shipsPlayer1[currentShipKey]['image'] = acorazadoUp
      shipsPlayer1[currentShipKey]['direction'] = "Up"
    elif rotate == 2:
      shipsPlayer1[currentShipKey]['image'] = acorazadoLeft
      shipsPlayer1[currentShipKey]['direction'] = "Left"
    elif rotate == 3:
      shipsPlayer1[currentShipKey]['image'] = acorazadoDown
      shipsPlayer1[currentShipKey]['direction'] = "Down"
    shipType = 3
    shipsPlayer1[currentShipKey]['type'] = "Acorazado"
    messagebox.showinfo("Data",shipsPlayer1) #//Solo para pruebas, quitar al final
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

# Colocar las naves //aun no se como funciona esta cosa
def actionPlayer1(x,y):
  """La función actionPlayer1 recibe la posición donde se van a colocar las naves del primer jugador y devuelve una imagen para dichas naves

  Args:
      x (_type_): _description_
      y (_type_): _description_
  """
  global buttonsMatrixPlayer1
  global shipType
  global shipCount
  global shipsPlayer1, currentShipIndex1, shipKeys1
  position = [x,y]
  currentShipKey = shipKeys1[currentShipIndex1] # Posición actual de la nave en el diccionario
  print (f"x={x},y={y}")
  if shipType == 1: #destructor
    if rotate == 0:
      buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
    elif rotate == 1:
      buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
    elif rotate == 2:
      buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
    elif rotate == 3:
      buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
  elif shipType == 2: #crucero
    if rotate == 0:
      buttonsMatrixPlayer1[y][x].configure(image=cruceroRight)
    elif rotate == 1:
      buttonsMatrixPlayer1[y][x].configure(image=cruceroUp)
    elif rotate == 2:
      buttonsMatrixPlayer1[y][x].configure(image=cruceroLeft)
    elif rotate == 3:
      buttonsMatrixPlayer1[y][x].configure(image=cruceroDown)
  elif shipType == 3: #acorazado
    if rotate == 0:
      buttonsMatrixPlayer1[y][x].configure(image=acorazadoRight)
    elif rotate == 1:
      buttonsMatrixPlayer1[y][x].configure(image=acorazadoUp)
    elif rotate == 2:
      buttonsMatrixPlayer1[y][x].configure(image=acorazadoLeft)
    elif rotate == 3:
      buttonsMatrixPlayer1[y][x].configure(image=acorazadoDown)
  # Asignar las cordenadas iniciales al barco
  shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
  currentShipIndex1 += 1
  onClickTrue()
  """if shipCount[0] < 9:
    shipCount[0] += 1
    print(f"Placed objects: {shipCount[0]}") #// solo para revisar, quitar al final
  if shipCount[0] == 9:
    # Desactivar todos los botones en esta matriz
    for row in buttonsMatrixPlayer1:
      for btn in row:
        btn.config(state="disabled")"""
  
def actionPlayer2(x,y):
  """La función actionPlayer2, recibe la posición donde se van a colocar las naves del segundo jugador y devuelve una imagen para dichas naves

  Args:
      x (_type_): _description_
      y (_type_): _description_
  """
  global buttonsMatrixPlayer2
  global shipType
  print (f"x={x},y={y}")
  if shipType == 1: #destructor
    if rotate == 0:
      buttonsMatrixPlayer2[y][x].configure(image=destructorRight)
    elif rotate == 1:
      buttonsMatrixPlayer2[y][x].configure(image=destructorUp)
    elif rotate == 2:
      buttonsMatrixPlayer2[y][x].configure(image=destructorLeft)
    elif rotate == 3:
      buttonsMatrixPlayer2[y][x].configure(image=destructorDown)
  elif shipType == 2: #crucero
    if rotate == 0:
      buttonsMatrixPlayer2[y][x].configure(image=cruceroRight)
    elif rotate == 1:
      buttonsMatrixPlayer2[y][x].configure(image=cruceroUp)
    elif rotate == 2:
      buttonsMatrixPlayer2[y][x].configure(image=cruceroLeft)
    elif rotate == 3:
      buttonsMatrixPlayer2[y][x].configure(image=cruceroDown)
  elif shipType == 3: #acorazado
    if rotate == 0:
      buttonsMatrixPlayer2[y][x].configure(image=acorazadoRight)
    elif rotate == 1:
      buttonsMatrixPlayer2[y][x].configure(image=acorazadoUp)
    elif rotate == 2:
      buttonsMatrixPlayer2[y][x].configure(image=acorazadoLeft)
    elif rotate == 3:
      buttonsMatrixPlayer2[y][x].configure(image=acorazadoDown)
 
def board(x: int, y: int) -> Tk:
  global buttonsMatrixPlayer1
  global buttonsMatrixPlayer2
  game = Tk()
  game.title("Piratas de Golfito")
  game.state("zoomed")
  windowWidth = x * 50
  windowHeight = y * 50
  game.geometry(f"{windowWidth}x{windowHeight}+0+0")
  shipsImages() # Se llama la función que asigna las imagenes a las varibles de los barcos.
  onClickTrue() # Se llama la función que permite el click
  # Calcular el tamaño de los botones en función del tamaño de la ventana y la cantidad de botones
  buttonWidth = windowWidth // x
  buttonHeight = windowHeight // y
  
  """shipCount = []
  if shipCount[0] < 9:
    shipCount[0] += 1
    print(f"Placed objects: {shipCount[0]}") #// solo para revisar, quitar al final
  if shipCount[0] == 9:
    # Desactivar todos los botones en esta matriz
    for row in buttonsMatrixPlayer1:
      for btn in row:
        btn.config(state="disabled")"""

  # Matrices de botones
  buttonsMatrixPlayer1 = [[Button(game, command=lambda x=c, y=f: actionPlayer1(x, y)) for c in range(x // 2)] for f in range(y)]
  buttonsMatrixPlayer2 = [[Button(game, command=lambda x=c, y=f: actionPlayer2(x, y)) for c in range(x // 2)] for f in range(y)]
  # Calcular el centro de cada mitad de la ventana
  centerX1 = 2.5 * windowWidth // 4
  centerX2 = 5 * windowWidth // 4
  # Calcular el inicio horizontal para que los botones estén centrados
  startX1 = centerX1 - (buttonWidth * (x // 4))
  startX2 = centerX2 - (buttonWidth * (x // 4))
  posy = 500
  # Colocar y configurar botones para la matríz del jugador 1
  for buttonsRow in buttonsMatrixPlayer1:
    posx = startX1
    for btn in buttonsRow:
        btn.place(x=posx, y=posy, height = buttonHeight, width = buttonWidth) #//falta acomodar las matrices en función de la cantidad de botones
        btn.configure(bg="#47A9CC")
        posx += buttonWidth
    posy += buttonHeight
  posy = 500
  # Colocar y configurar botones para la matríz del jugador 2
  for buttonsRow in buttonsMatrixPlayer2:
    posx = startX2
    for btn in buttonsRow:
        btn.place(x=posx, y=posy, height = buttonHeight, width = buttonWidth)
        btn.configure(bg="#47A9CC")
        posx += buttonWidth
    posy += buttonHeight
  return game
game = board(boardColumns(),boardRows())

##KeyBinds##
game.bind("<KeyPress-q>", lambda event : selectShip1(event))
game.bind("<KeyPress-w>", lambda event : selectShip2(event))
game.bind("<KeyPress-e>", lambda event : selectShip3(event))
on_press_key("r", rotateShip)

game.mainloop()