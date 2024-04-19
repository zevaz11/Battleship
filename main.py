from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

buttonsMatrixPlayer1=[]
buttonsMatrixPlayer2=[]
shipCount = []
rotate = 0
##Diccionarios con la información de los barcos##
shipsPlayer1 = {
  #Destructores
  "ship1" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship2" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship3" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship4" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship5" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship6" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  #Cruceros
  "ship7" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship8" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship9" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship10": {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  #Acorazados
  "ship11": {"visibility": True, "movibility": True, "alive": True, "type": "Acorazado", "direction": "Right", "position":[[],[],[]]},
  "ship12": {"visibility": True, "movibility": True, "alive": True, "type": "Acorazado", "direction": "Right", "position":[[],[],[]]}
}
shipsPlayer2 = {
  #Destructores
  "ship1" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship2" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship3" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship4" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship5" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  "ship6" : {"visibility": True, "movibility": True, "alive": True, "type": "Destructor", "direction": "Right", "position":[]},
  #Cruceros
  "ship7" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship8" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship9" : {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  "ship10": {"visibility": True, "movibility": True, "alive": True, "type": "Crucero", "direction": "Right", "position":[[],[]]},
  #Acorazados
  "ship11": {"visibility": True, "movibility": True, "alive": True, "type": "Acorazado", "direction": "Right", "position":[[],[],[]]},
  "ship12": {"visibility": True, "movibility": True, "alive": True, "type": "Acorazado", "direction": "Right", "position":[[],[],[]]}
}

##Variables de los barcos##
shipType = 1 #maneja el tipo de nave
#acorazado
destructorRight = Image.open("b1.png")
destructorUp = Image.open("b1.png")
destructorUp = destructorUp.rotate(90)
destructorLeft = Image.open("b1.png")
destructorLeft = destructorLeft.rotate(180)
destructorDown = Image.open("b1.png")
destructorDown = destructorDown.rotate(270)

#crucero
cruceroRight = Image.open("b22.png")
cruceroRight2 = Image.open("b21.png")
#
cruceroUp = Image.open("b22.png")
cruceroUp = cruceroUp.rotate(90)
cruceroUp2 = Image.open("b21.png")
cruceroUp2 = cruceroUp.rotate(90)
#
cruceroLeft = Image.open("b22.png")
cruceroLeft = cruceroLeft.rotate(180)
cruceroLeft2 = Image.open("b21.png")
cruceroLeft2 = cruceroLeft.rotate(180)
#
cruceroDown = Image.open("b22.png")
cruceroDown = cruceroDown.rotate(270)
cruceroDown2 = Image.open("b21.png")
cruceroDown2 = cruceroDown.rotate(270)

#acorazado
acorazadoRight = Image.open("b33.png")
acorazadoRight2 = Image.open("b32.png")
acorazadoRight3 = Image.open("b31.png")
#
acorazadoUp = Image.open("b33.png")
acorazadoUp = acorazadoUp.rotate(90)
acorazadoUp2 = Image.open("b32.png")
acorazadoUp2 = acorazadoUp.rotate(90)
acorazadoUp3 = Image.open("b31.png")
acorazadoUp3 = acorazadoUp.rotate(90)
#
acorazadoLeft = Image.open("b33.png")
acorazadoLeft = acorazadoLeft.rotate(180)
acorazadoLeft2 = Image.open("b32.png")
acorazadoLeft2 = acorazadoLeft.rotate(180)
acorazadoLeft3 = Image.open("b31.png")
acorazadoLeft3 = acorazadoLeft.rotate(180)
#
acorazadoDown = Image.open("b33.png")
acorazadoDown = acorazadoDown.rotate(270)
acorazadoDown2 = Image.open("b32.png")
acorazadoDown2 = acorazadoDown.rotate(270)
acorazadoDown3 = Image.open("b31.png")
acorazadoDown3 = acorazadoDown.rotate(270)

##Funciones KeyBinds##
def rotateShip(event):
  global rotate
  rotate += 1
  if rotate > 3:
    rotate = 0

def selectShip1(event):
  global destructorRight
  global destructorUp
  global destructorLeft
  global destructorDown
  global rotate
  global shipType
  if rotate == 0:
    destructorRight = destructorRight.resize((50,50))
    destructorRight = ImageTk.PhotoImage(destructorRight)
  elif rotate == 1:
    destructorUp = destructorUp.resize((50,50))
    destructorUp = ImageTk.PhotoImage(destructorUp)
    shipsPlayer1
  elif rotate == 2:
    destructorLeft = destructorLeft.resize((50,50))
    destructorLeft = ImageTk.PhotoImage(destructorLeft)
  elif rotate == 3:
    destructorDown = destructorDown.resize((50,50))
    destructorDown = ImageTk.PhotoImage(destructorDown)
  shipType = 1

def selectShip2(event):
  global cruceroRight
  global cruceroRight2
  global cruceroUp
  global cruceroUp2
  global cruceroLeft
  global cruceroLeft2
  global cruceroDown
  global cruceroDown2
  global rotate
  global shipType
  if rotate == 0:
    cruceroRight = cruceroRight.resize((50,50))
    cruceroRight = ImageTk.PhotoImage(cruceroRight)
  elif rotate == 1:
    cruceroUp = cruceroUp.resize((50,50))
    cruceroUp = ImageTk.PhotoImage(cruceroUp)
  elif rotate == 2:
    cruceroLeft = cruceroLeft.resize((50,50))
    cruceroLeft = ImageTk.PhotoImage(cruceroLeft)
  elif rotate == 3:
    cruceroDown = cruceroDown.resize((50,50))
    cruceroDown = ImageTk.PhotoImage(cruceroDown)
  shipType = 2

def selectShip3(event):
  global acorazadoRight
  global acorazadoRight2
  global acorazadoRight3
  global acorazadoUp
  global acorazadoUp2
  global acorazadoUp3
  global acorazadoLeft
  global acorazadoLeft2
  global acorazadoLeft3
  global acorazadoDown
  global acorazadoDown2
  global acorazadoDown3
  global rotate
  global shipType
  if rotate == 0:
    acorazadoRight = acorazadoRight.resize((50,50))
    acorazadoRight = ImageTk.PhotoImage(acorazadoRight)
  elif rotate == 1:
    acorazadoUp = acorazadoUp.resize((50,50))
    acorazadoUp = ImageTk.PhotoImage(acorazadoUp)
  elif rotate == 2:
    acorazadoLeft = acorazadoLeft.resize((50,50))
    acorazadoLeft = ImageTk.PhotoImage(acorazadoLeft)
  elif rotate == 3:
    acorazadoDown = acorazadoDown.resize((50,50))
    acorazadoDown = ImageTk.PhotoImage(acorazadoDown)
  shipType = 3

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
  print (f"x={x},y={y}")
  if shipType == 1: #destructor
    if rotate == 0:
      buttonsMatrixPlayer1[y][x].configure(image=destructorRight)
    elif rotate == 1:
      buttonsMatrixPlayer1[y][x].configure(image=destructorUp)
    elif rotate == 2:
      buttonsMatrixPlayer1[y][x].configure(image=destructorLeft)
    elif rotate == 3:
      buttonsMatrixPlayer1[y][x].configure(image=destructorDown)
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
  if shipCount[0] < 9:
    shipCount[0] += 1
    print(f"Placed objects: {shipCount[0]}") #// solo para revisar, quitar al final
  if shipCount[0] == 9:
    # Desactivar todos los botones en esta matriz
    for row in buttonsMatrixPlayer1:
      for btn in row:
        btn.config(state="disabled")
  
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
  # Calcular el tamaño de los botones en función del tamaño de la ventana y la cantidad de botones
  buttonWidth = windowWidth // x
  buttonHeight = windowHeight // y
  
  shipCount = []
  if shipCount[0] < 9:
    shipCount[0] += 1
    print(f"Placed objects: {shipCount[0]}") #// solo para revisar, quitar al final
  if shipCount[0] == 9:
    # Desactivar todos los botones en esta matriz
    for row in buttonsMatrixPlayer1:
      for btn in row:
        btn.config(state="disabled")

  """# Calcular el ancho de cada mitad del tablero y el margen
  halfWidth = (x // 2) * 50
  margin = 50  # margen entre los dos grupos de botones"""
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
shipImage = game.bind("<KeyPress-q>", lambda event : selectShip1(event))
shipImage = game.bind("<KeyPress-w>", lambda event : selectShip2(event))
shipImage = game.bind("<KeyPress-e>", lambda event : selectShip3(event))
on_press_key("r", rotateShip)

game.mainloop()