from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

keyS = True
buttonsMatrixPlayer1= []
buttonsMatrixPlayer2= []
matrixPlayer1 = []
matrixPlayer2 = []
shipCount = []
rotate = 0

#Contadores de naves de cada jugador
totalShipsPlayer1 = 0
totalShipsPlayer2 = 0
destructorsPlayer1 = 0
crucerosPlayer1 = 0
acorazadosPlayer1 = 0
destructorsPlayer2 = 0
crucerosPlayer2 = 0
acorazadosPlayer2 = 0

##Diccionarios con la información de los barcos##
currentShipIndex1 = 0
currentShipIndex2 = 0
shipsPlayer1 = {
  "ship1" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship2" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship3" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship4" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship5" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship6" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship7" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship8" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship9" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship10": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship11": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship12": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""}
}
shipsPlayer2 = {
  "ship1" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship2" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship3" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship4" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship5" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship6" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship7" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship8" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship9" : {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship10": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship11": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""},
  "ship12": {"visibility": True, "mobility": True, "alive": True, "type": "", "direction": "", "position":[0,0], "image": ""}
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
  acorazadoUp2 = acorazadoUp2.rotate(90)
  acorazadoUp3 = acorazadoRight3.resize((50,50))
  acorazadoUp3 = acorazadoUp3.rotate(90)
  #
  acorazadoLeft = acorazadoRight.resize((50,50))
  acorazadoLeft = acorazadoLeft.rotate(180)
  acorazadoLeft2 = acorazadoRight2.resize((50,50))
  acorazadoLeft2 = acorazadoLeft2.rotate(180)
  acorazadoLeft3 = acorazadoRight3.resize((50,50))
  acorazadoLeft3 = acorazadoLeft3.rotate(180)
  #
  acorazadoDown = acorazadoRight.resize((50,50))
  acorazadoDown = acorazadoDown.rotate(270)
  acorazadoDown2 = acorazadoRight2.resize((50,50))
  acorazadoDown2 = acorazadoDown2.rotate(270)
  acorazadoDown3 = acorazadoRight3.resize((50,50))
  acorazadoDown3 = acorazadoDown3.rotate(270)
  #
  acorazadoRight = ImageTk.PhotoImage(acorazadoRight)
  acorazadoRight2= ImageTk.PhotoImage(acorazadoRight2)
  acorazadoRight3= ImageTk.PhotoImage(acorazadoRight3)
  acorazadoUp = ImageTk.PhotoImage(acorazadoUp)
  acorazadoUp2 = ImageTk.PhotoImage(acorazadoUp2)
  acorazadoUp3 = ImageTk.PhotoImage(acorazadoUp3)
  acorazadoLeft = ImageTk.PhotoImage(acorazadoLeft)
  acorazadoLeft2 = ImageTk.PhotoImage(acorazadoLeft2)
  acorazadoLeft3 = ImageTk.PhotoImage(acorazadoLeft3)
  acorazadoDown = ImageTk.PhotoImage(acorazadoDown)
  acorazadoDown2 = ImageTk.PhotoImage(acorazadoDown2)
  acorazadoDown3 = ImageTk.PhotoImage(acorazadoDown3)
  
def onClickTrue(): # Permite que la Q, W y E puedan volver a ser usadas para seleccionar otro barco, pero solo despues de que el barco anterior sea colocado.
  global  keyQ, keyW, keyE
  keyQ = keyW = keyE = True 
def onClickFalse(): # Desactiva las teclas Q, W y R para que no puedan volver a ser usadas hasta que se coloque el barco seleccionado
  global  keyQ, keyW, keyE
  keyQ = keyW = keyE = False

##Buscar colisiones##
def duplicatePosition(baseShipPosition):
  global shipsPlayer1
  global shipKeys1
  currentShipIndex1 = 0
  currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
  basePosition = tuple(baseShipPosition)
  element = 0
  while element < len(shipsPlayer1):
    currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
    currentPosition = tuple(shipsPlayer1[currentShipKey]["position"])
    if currentPosition == basePosition:
      return False
    # Revisión en Y
    elif currentPosition[1] == basePosition[1]+1:
      return True
    elif currentPosition[1] == basePosition[1]+2:
      return True
    elif currentPosition[1] == basePosition[1]-1:
      return True
    elif currentPosition[1] == basePosition[1]-2:
      return True
    # Revisión en X
    elif currentPosition[0] == basePosition[0]+1:
      return True
    elif currentPosition[0] == basePosition[0]+2:
      return True
    elif currentPosition[0] == basePosition[0]-1:
      return True
    elif currentPosition[0] == basePosition[0]-2:
      return True
    currentShipIndex1 += 1
    element += 1
  return False

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
  global destructorsPlayer1, totalShipsPlayer1
  global keyQ
  if destructorsPlayer1 >= 6:
    messagebox.showinfo("Advertencia","Ya colocó todos los destructores")
  elif keyQ == True:
    destructorsPlayer1 += 1
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
    totalShipsPlayer1 += 1
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def selectShip2(event):
  global cruceroRight, cruceroRight2, cruceroUp, cruceroUp2, cruceroLeft, cruceroLeft2, cruceroDown, cruceroDown2 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global crucerosPlayer1, totalShipsPlayer1
  global keyW
  if crucerosPlayer1 >= 4:
    messagebox.showinfo("Advertencia","Ya colocó todos los cruceros")
  elif keyW == True:
    crucerosPlayer1 += 1
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
    totalShipsPlayer1 += 1
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def selectShip3(event):
  global acorazadoRight, acorazadoRight2, acorazadoRight3, acorazadoUp, acorazadoUp2, acorazadoUp3, acorazadoLeft, acorazadoLeft2, acorazadoLeft3, acorazadoDown, acorazadoDown2, acorazadoDown3 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global acorazadosPlayer1, totalShipsPlayer1
  global keyE
  if acorazadosPlayer1 >= 2:
    messagebox.showinfo("Advertencia","Ya colocó todos los acorazados")
  elif keyE == True:
    acorazadosPlayer1 += 1
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
    totalShipsPlayer1 +=1
    onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def startGame(event):
  global currentShipIndex1, currentShipIndex2
  global keyS
  if keyS == True:
    currentShipIndex1 = currentShipIndex2 = 0
  else:
    pass

def shipMovement(event):
  global shipsPlayer1, shipsPlayer2, shipKeys1, shipKeys2, currentShipIndex1, currentShipIndex2, matrixPlayer1, matrixPlayer2
  global destructorRight, destructorUp, destructorLeft, destructorDown
  global cruceroRight, cruceroRight2, cruceroUp, cruceroUp2, cruceroLeft, cruceroLeft2, cruceroDown, cruceroDown2
  global acorazadoRight, acorazadoRight2, acorazadoRight3, acorazadoUp, acorazadoUp2, acorazadoUp3, acorazadoLeft, acorazadoLeft2, acorazadoLeft3, acorazadoDown, acorazadoDown2, acorazadoDown3
  # ShipKey, son listas que almacenan las naves de cada diccionario de cada jugador
  currentShipIndex1 = 0 #// Esto es temporal
  currentShipIndex2 = 0 #// Esto es temporal
  currentShipKey = shipKeys1[currentShipIndex1] # En la variable currentShipKey, se guarda el valor de la posición del diccionario que vamos a revisar
  element = 0
  while element < len(shipKeys1):
    currentShipKey = shipKeys1[currentShipIndex1] # En la variable currentShipKey, se guarda el valor de la posición del diccionario que vamos a revisar
    actualPosition = shipsPlayer1[currentShipKey]["position"] # actualPosition, va a almacenar la posición actual de la nave
    newPosition = actualPosition # es la variable que va a almacenar la nueva posición que va a tener la nave
    # Primero, revisamos si la nave aun no ha sido destruida
    if shipsPlayer1[currentShipKey]["alive"] == True: # Creo que esto es descartable, porque para el movimiento no nos importa si está vivo o no, solo si se puede mover
      # Segundo, revisamos si la nave no ha recibido daños y por ende, aún se puede mover
      if shipsPlayer1[currentShipKey]["mobility"] == True:
        # Destructor
        if shipsPlayer1[currentShipKey]["type"] == "Destructor":
          ##Revisión de avance, derecha##
          if shipsPlayer1[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = destructorLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]+1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: 
              newPosition[0] += 1 # x+1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = destructorLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:
              newPosition[0] += 2 # x+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-2].configure(image="")
          ##Revisión de avance, arriba##
          elif shipsPlayer1[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = destructorDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]-1 == matrixPlayer1[0][0]: 
              newPosition[1] -= 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+1][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = destructorDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:
              newPosition[1] -= 2 # y-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+2][newPosition[0]].configure(image="")
          ##Revisión de avance, izquierda##
          elif shipsPlayer1[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = destructorRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]-1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: 
              newPosition[0] -= 1 # x-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = destructorRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:  
              newPosition[0] -= 2 # x-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+2].configure(image="")
          ##Revisión de avance, abajo##
          elif shipsPlayer1[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = destructorUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]+1 == matrixPlayer1[-1][-1]: 
              newPosition[1] += 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-1][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = destructorUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:  
              newPosition[1] += 2 # y+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-2][newPosition[0]].configure(image="")
        # Crucero
        elif shipsPlayer1[currentShipKey]["type"] == "Crucero":
          ##Revisión de avance, derecha##
          if shipsPlayer1[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = cruceroLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]+1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: 
              newPosition[0] += 1 # x+1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-1].configure(image="")

            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = cruceroLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Si no tiene ninguna limitación
            else:
              newPosition[0] += 2 # x+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-2].configure(image="")
          ##Revisión de avance, arriba##
          elif shipsPlayer1[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = cruceroDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]-1 == matrixPlayer1[0][0]: 
              newPosition[1] -= 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+1][newPosition[0]].configure(image="")

            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = cruceroDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Si no tiene ninguna limitación
            else:
              newPosition[1] -= 2 # y-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+2][newPosition[0]].configure(image="")
          ##Revisión de avance, izquierda##
          elif shipsPlayer1[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = cruceroRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]-1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: 
              newPosition[0] -= 1 # x-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+1].configure(image="")

            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = cruceroRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Si no tiene ninguna limitación
            else:  
              newPosition[0] -= 2 # x-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+2].configure(image="")
          ##Revisión de avance, abajo##
          elif shipsPlayer1[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = cruceroUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]+1 == matrixPlayer1[-1][-1]: 
              newPosition[1] += 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-1][newPosition[0]].configure(image="")

            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = cruceroUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])

            # Si no tiene ninguna limitación
            else:  
              newPosition[1] += 2 # y+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-2][newPosition[0]].configure(image="")
        # Acorazado
        elif shipsPlayer1[currentShipKey]["type"] == "Acorazado":
          ##Revisión de avance, derecha##
          if shipsPlayer1[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = acorazadoLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]+1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][-1]: 
              newPosition[0] += 1 # x+1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = acorazadoLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:
              newPosition[0] += 2 # x+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-2].configure(image="")
          ##Revisión de avance, arriba##
          elif shipsPlayer1[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = acorazadoDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]-1 == matrixPlayer1[0][0]: 
              newPosition[1] -= 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+1][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = acorazadoDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:
              newPosition[1] -= 2 # y-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+2][newPosition[0]].configure(image="")
          ##Revisión de avance, izquierda##
          elif shipsPlayer1[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer1[currentShipKey]["position"][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = acorazadoRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][0]-1 == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1]][0]: 
              newPosition[0] -= 1 # x-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = acorazadoRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:  
              newPosition[0] -= 2 # x-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+2].configure(image="")
          ##Revisión de avance, abajo##
          elif shipsPlayer1[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1] == matrixPlayer1[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = acorazadoUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer1[currentShipKey]["position"][1]+1 == matrixPlayer1[-1][-1]: 
              newPosition[1] += 1 # y-1
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-1][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = acorazadoUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación
            else:  
              newPosition[1] += 2 # y+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-2][newPosition[0]].configure(image="")
    currentShipIndex1 += 1 
    element += 1
    
# Colocar las naves
def actionPlayer1(x,y):
  """La función actionPlayer1 recibe la posición donde se van a colocar las naves del primer jugador y devuelve una imagen para dichas naves

  Args:
      x (int): posición donde se hizo click de la coordenada x
      y (int): posición donde se hizo click de la coordenada y
  """
  global buttonsMatrixPlayer1
  global shipType
  global shipCount
  global shipsPlayer1, currentShipIndex1, shipKeys1
  position = [x,y]
  currentShipKey = shipKeys1[currentShipIndex1] # Posición actual de la nave en el diccionario
  print (f"x={x},y={y}")
  if totalShipsPlayer1 <= 12:  
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
        buttonsMatrixPlayer1[y][x+1].configure(image=cruceroRight2)
        position = [[x,y],[x+1,y]]
      elif rotate == 1:
        buttonsMatrixPlayer1[y][x].configure(image=cruceroUp)
        buttonsMatrixPlayer1[y-1][x].configure(image=cruceroUp2)
        position = [[x,y],[x,y-1]]
      elif rotate == 2:
        buttonsMatrixPlayer1[y][x].configure(image=cruceroLeft)
        buttonsMatrixPlayer1[y][x-1].configure(image=cruceroLeft2)
        position = [[x,y],[x-1,y]]
      elif rotate == 3:
        buttonsMatrixPlayer1[y][x].configure(image=cruceroDown)
        buttonsMatrixPlayer1[y+1][x].configure(image=cruceroDown2)
        position = [[x,y],[x,y+1]]
    elif shipType == 3: #acorazado
      if rotate == 0:
        buttonsMatrixPlayer1[y][x].configure(image=acorazadoRight)
        buttonsMatrixPlayer1[y][x+1].configure(image=acorazadoRight2)
        buttonsMatrixPlayer1[y][x+2].configure(image=acorazadoRight3)
        position = [[x,y],[x+1,y],[x+2,y]]
      elif rotate == 1:
        buttonsMatrixPlayer1[y][x].configure(image=acorazadoUp)
        buttonsMatrixPlayer1[y-1][x].configure(image=acorazadoUp2)
        buttonsMatrixPlayer1[y-2][x].configure(image=acorazadoUp3)
        position = [[x,y],[x,y-1],[x,y-2]]
      elif rotate == 2:
        buttonsMatrixPlayer1[y][x].configure(image=acorazadoLeft)
        buttonsMatrixPlayer1[y][x-1].configure(image=acorazadoLeft2)
        buttonsMatrixPlayer1[y][x-2].configure(image=acorazadoLeft3)
        position = [[x,y],[x-1,y],[x-2,y]]
      elif rotate == 3:
        buttonsMatrixPlayer1[y][x].configure(image=acorazadoDown)
        buttonsMatrixPlayer1[y+1][x].configure(image=acorazadoDown2)
        buttonsMatrixPlayer1[y+2][x].configure(image=acorazadoDown3)
        position = [[x,y],[x,y+1],[x,y+2]]
        
  else:
    messagebox.showinfo("Advertencia","El jugador 1 ya colocó todas sus naves")
  # Asignar las cordenadas iniciales al barco
  shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
  currentShipIndex1 += 1
  onClickTrue() # Para volver a habilitar la selección de barcos
  
def actionPlayer2(x,y):
  """La función actionPlayer2, recibe la posición donde se van a colocar las naves del segundo jugador y devuelve una imagen para dichas naves

  Args:
      x (int): posición donde se hizo click de la coordenada x
      y (int): posición donde se hizo click de la coordenada y
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

# Generación del tablero
def board(x: int, y: int) -> Tk:
  global buttonsMatrixPlayer1, buttonsMatrixPlayer2, matrixPlayer1, matrixPlayer2
  global currentShipIndex1
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

  # Matrices de botones
  buttonsMatrixPlayer1 = [[Button(game, command=lambda x=c, y=f: actionPlayer1(x, y)) for c in range(x // 2)] for f in range(y)]
  matrixPlayer1 = [[c for c in range(x // 2)] for f in range(y)]
  buttonsMatrixPlayer2 = [[Button(game, command=lambda x=c, y=f: actionPlayer2(x, y)) for c in range(x // 2)] for f in range(y)]
  matrixPlayer2 = [[c for c in range(x // 2)] for f in range(y)]
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

# Iniciar el juego
#game.bind("<KeyPress-t>", lambda event : startGame(event)) colocar cuando se haga el sistema de transición entre eventos
game.bind("<KeyPress-t>", lambda event : shipMovement(event))

game.mainloop()

# 1 Una función para que se bloquee el tablero del jugador 2 hasta que el jugador 1 termine de colocar sus naves
# 2 Una función para que se bloquee el tablero del jugador 1 cuando termine de colocar sus piezas y permita usar el tablero del jugador 2
# 3 Modificar las funciones actuales para que puedan alterar el tablero del jugador 2 y modificar las entradas del diccionario
# 4 Hacer la función para el movimiento de las naves.
# 4.1 Tiene que revisar si la nave se puede mover.
# 4.2 Revisar si la nave llegó a un borde del tablero y debe de hacer que se devuelva.
# 4.3 Va a revisar la posición de cada nave haciendo el recorrido por cada diccionario y revisando la llave: "position"