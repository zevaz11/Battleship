from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image
from tkinter.font import *

keyS = True
buttonsMatrixPlayer1= []
buttonsMatrixPlayer2= []
matrixPlayer1 = []
matrixPlayer2 = []
shipCount = []
rotate = 0
#texto
actualText = "Battleship"
family = "Terminal",
size = 30
color = "black"
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
##Llaves de las listas##
shipKeys1 = list(shipsPlayer1.keys())
shipKeys2 = list(shipsPlayer2.keys())

##Variables de los barcos##
shipType = 0 #maneja el tipo de nave
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
  global  keyQ, keyW, keyE, shipType
  keyQ = keyW = keyE = True
  shipType = 0
def onClickFalse(): # Desactiva las teclas Q, W y R para que no puedan volver a ser usadas hasta que se coloque el barco seleccionado
  global  keyQ, keyW, keyE
  keyQ = keyW = keyE = False

##Buscar colisiones##
def checkPositionDestructor(baseShipPosition):
  global shipsPlayer1
  global shipKeys1
  currentShipIndex1 = 0
  currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
  basePosition = baseShipPosition
  element = 0
  baseDirection = shipsPlayer1[currentShipKey]["direction"]
  while element < len(shipsPlayer1):
    currentShipKey = shipKeys1[currentShipIndex1] # Posición actual en el diccionario 
    currentPosition = shipsPlayer1[currentShipKey]["position"]
    print(basePosition)
    print(currentPosition)
    if baseDirection == "Right": #Derecha 
      basePosition[0]+1
      if currentPosition == basePosition:
        return True
      else:
        basePosition[0]-1
    elif baseDirection == "Up": # Arriba
      basePosition[1]-1
      if currentPosition == basePosition:
        return True
      else:
        basePosition[1]+1
    if baseDirection == "Left": #Derecha 
      basePosition[0]-1
      if currentPosition == basePosition:
        return True
      else:
        basePosition[0]+1
    elif baseDirection == "Down": #Abajo
      basePosition[1]-1
      if currentPosition == basePosition:
        return True
      else:
        basePosition[1]+1
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
  global destructorsPlayer1, totalShipsPlayer1, destructorsPlayer2, totalShipsPlayer2
  global keyQ
  if totalShipsPlayer1 < 12:
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
      totalShipsPlayer1 += 1
      onClickFalse()
  elif totalShipsPlayer1 >= 12:
    if destructorsPlayer2 >= 6:
      messagebox.showinfo("Advertencia","Ya colocó todos los destructores")
    elif keyQ == True:
      destructorsPlayer2 += 1
      currentShipKey = shipKeys2[currentShipIndex2] # Posición actual en el diccionario 
      if rotate == 0:
        shipsPlayer2[currentShipKey]['image'] = destructorRight
        shipsPlayer2[currentShipKey]['direction'] = "Right"
      elif rotate == 1:
        shipsPlayer2[currentShipKey]['image'] = destructorUp
        shipsPlayer2[currentShipKey]['direction'] = "Up"
      elif rotate == 2:
        shipsPlayer2[currentShipKey]['image'] = destructorLeft
        shipsPlayer2[currentShipKey]['direction'] = "Left"
      elif rotate == 3:
        shipsPlayer2[currentShipKey]['image'] = destructorDown
        shipsPlayer2[currentShipKey]['direction'] = "Down"
      shipType = 1
      shipsPlayer2[currentShipKey]['type'] = "Destructor"
      totalShipsPlayer2 += 1
      onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")

def selectShip2(event):
  global cruceroRight, cruceroRight2, cruceroUp, cruceroUp2, cruceroLeft, cruceroLeft2, cruceroDown, cruceroDown2 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global crucerosPlayer1, totalShipsPlayer1, crucerosPlayer2, totalShipsPlayer2
  global keyW
  if totalShipsPlayer1 < 12:
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

      totalShipsPlayer1 += 1
      onClickFalse()
  elif totalShipsPlayer1 >= 12:
    if crucerosPlayer2 >= 4:
      messagebox.showinfo("Advertencia","Ya colocó todos los cruceros")
    elif keyW == True:
      crucerosPlayer2 += 1
      currentShipKey = shipKeys2[currentShipIndex2] # Posición actual en el diccionario 
      if rotate == 0:
        shipsPlayer2[currentShipKey]['image'] = cruceroRight
        shipsPlayer2[currentShipKey]['direction'] = "Right"
      elif rotate == 1:
        shipsPlayer2[currentShipKey]['image'] = cruceroUp
        shipsPlayer2[currentShipKey]['direction'] = "Up"
      elif rotate == 2:
        shipsPlayer2[currentShipKey]['image'] = cruceroLeft
        shipsPlayer2[currentShipKey]['direction'] = "Left"
      elif rotate == 3:
        shipsPlayer2[currentShipKey]['image'] = cruceroDown
        shipsPlayer2[currentShipKey]['direction'] = "Down"
      shipType = 2
      shipsPlayer2[currentShipKey]['type'] = "Crucero"

      totalShipsPlayer2 += 1
      onClickFalse()
  else:
    messagebox.showinfo("Advertencia", "Debe de colocar el barco antes de seleccionar otro")
  

def selectShip3(event):
  global acorazadoRight, acorazadoRight2, acorazadoRight3, acorazadoUp, acorazadoUp2, acorazadoUp3, acorazadoLeft, acorazadoLeft2, acorazadoLeft3, acorazadoDown, acorazadoDown2, acorazadoDown3 #Posiciones barcos
  global shipsPlayer1, rotate, shipType, currentShipIndex1, currentShipIndex2 #Parametros de los barcos
  global shipKeys1, shipKeys2 #listas con las llaves de los diccionarios
  global acorazadosPlayer1, totalShipsPlayer1, acorazadosPlayer2, totalShipsPlayer2
  global keyE
  if totalShipsPlayer1 < 12:
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

      totalShipsPlayer1 +=1
      onClickFalse()
  elif totalShipsPlayer2 <= 12:
    if acorazadosPlayer2 >= 2:
      messagebox.showinfo("Advertencia","Ya colocó todos los acorazados")
    elif keyE == True:
      acorazadosPlayer2 += 1
      currentShipKey = shipKeys2[currentShipIndex2] # Posición actual en el diccionario 
      if rotate == 0:
        shipsPlayer2[currentShipKey]['image'] = acorazadoRight
        shipsPlayer2[currentShipKey]['direction'] = "Right"
      elif rotate == 1:
        shipsPlayer2[currentShipKey]['image'] = acorazadoUp
        shipsPlayer2[currentShipKey]['direction'] = "Up"
      elif rotate == 2:
        shipsPlayer2[currentShipKey]['image'] = acorazadoLeft
        shipsPlayer2[currentShipKey]['direction'] = "Left"
      elif rotate == 3:
        shipsPlayer2[currentShipKey]['image'] = acorazadoDown
        shipsPlayer2[currentShipKey]['direction'] = "Down"
      shipType = 3
      shipsPlayer2[currentShipKey]['type'] = "Acorazado"
      totalShipsPlayer2 +=1
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
  currentShipIndex1 = 0 
  currentShipIndex2 = 0 
  currentShipKey = shipKeys1[currentShipIndex1] # En la variable currentShipKey, se guarda el valor de la posición del diccionario que vamos a revisar
  element = 0
  #movimiento primer jugador
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
            else:
              newPosition[0] += 2 # x+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]-2].configure(image="")
            """elif checkPositionDestructor(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = destructorLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
            # Si no tiene ninguna limitación"""
            
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
            # Si no tiene ninguna limitación
            else:
              newPosition[1] -= 2 # y-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]+2][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = destructorDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
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
            # Si no tiene ninguna limitación
            else:  
              newPosition[0] -= 2 # x-2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]+2].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = destructorRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
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
            # Si no tiene ninguna limitación
            else:  
              newPosition[1] += 2 # y+2
              shipsPlayer1[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])
              buttonsMatrixPlayer1[newPosition[1]-2][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = destructorUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
        # Crucero
        elif shipsPlayer1[currentShipKey]["type"] == "Crucero":
          ##Revisión de avance, derecha##
          if shipsPlayer1[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer1[currentShipKey]["position"][1][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][1][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = cruceroLeft
              newPosition[0][0] += 1
              newPosition[1][0] -= 1
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroLeft)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroLeft2)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][0] += 1 # trasero x+1
              newPosition[1][0] += 1 # frente x+1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroRight2)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroRight)
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = cruceroLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
          ##Revisión de avance, arriba##
          elif shipsPlayer1[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1][1] == matrixPlayer1[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = cruceroDown
              newPosition[0][1] -= 1
              newPosition[1][1] += 1
              
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroDown)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroDown2)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][1] -= 1 # y-1
              newPosition[1][1] -= 1 # y-1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroUp)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroUp2)
              buttonsMatrixPlayer1[newPosition[0][1]+1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = cruceroDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
          ##Revisión de avance, izquierda##
          elif shipsPlayer1[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer1[currentShipKey]["position"][1][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][0][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = cruceroRight
              newPosition[0][0] -= 1
              newPosition[1][0] += 1
              
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroRight)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroRight2)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][0] -= 1 # trasero x-1
              newPosition[1][0] -= 1 # frente x-1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroLeft)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroLeft2)
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]+1].configure(image="")
          ##Revisión de avance, abajo##
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = cruceroRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
          elif shipsPlayer1[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][1][1] == matrixPlayer1[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = cruceroUp
              newPosition[0][1] += 1
              newPosition[1][1] -= 1
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroUp)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroUp2)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][1] += 1 # y+1
              newPosition[1][1] += 1 # y+1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroDown2)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroDown)
              buttonsMatrixPlayer1[newPosition[0][1]-1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = cruceroUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
        # Acorazado
        elif shipsPlayer1[currentShipKey]["type"] == "Acorazado":
          ##Revisión de avance, derecha##
          if shipsPlayer1[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer1[currentShipKey]["position"][2][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][2][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = acorazadoLeft
              newPosition[0][0] += 2
              newPosition[2][0] -= 2
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoLeft)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoLeft2)
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoLeft3)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][0] += 1 # trasero x+1
              newPosition[1][0] += 1 # medio x+1
              newPosition[2][0] += 1 # frente x+1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoRight3)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoRight2)
              shipsPlayer1[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoRight)
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Left"
              shipsPlayer1[currentShipKey]["image"] = acorazadoLeft
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""

          ##Revisión de avance, arriba##
          elif shipsPlayer1[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][2][1] == matrixPlayer1[0][0]: #revisa si se encuentra en el borde superior del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = acorazadoDown
              newPosition[0][1] -= 2
              newPosition[2][1] += 2
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoDown)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoDown2)
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoDown3)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][1] -= 1 # y-1
              newPosition[1][1] -= 1 # y-1
              newPosition[2][1] -= 1 # y-1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoUp)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoUp2)
              shipsPlayer1[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoUp3)
              buttonsMatrixPlayer1[newPosition[0][1]+1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Down"
              shipsPlayer1[currentShipKey]["image"] = acorazadoDown
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
          ##Revisión de avance, izquierda##
          elif shipsPlayer1[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer1[currentShipKey]["position"][2][0] == matrixPlayer1[shipsPlayer1[currentShipKey]["position"][0][1]][0]:
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = acorazadoRight
              newPosition[0][0] -= 2
              newPosition[2][0] += 2
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoRight)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoRight2)
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoRight3)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][0] -= 1 # trasero x-1
              newPosition[1][0] -= 1 # medio x-1
              newPosition[2][0] -= 1 # frente x-1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoLeft)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoLeft2)
              shipsPlayer1[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoLeft3)
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]+1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Right"
              shipsPlayer1[currentShipKey]["image"] = acorazadoRight
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
          ##Revisión de avance, abajo##
          elif shipsPlayer1[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer1[currentShipKey]["position"][2][1] == matrixPlayer1[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = acorazadoUp
              newPosition[0][1] += 2
              newPosition[2][1] -= 2
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoUp)
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoUp2)
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoUp3)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][1] += 1 # y+1
              newPosition[1][1] += 1 # y+1
              newPosition[2][1] += 1 # y+1
              shipsPlayer1[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer1[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoDown3)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoDown2)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoDown)
              shipsPlayer1[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer1[newPosition[0][1]-1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer1[currentShipKey]["position"]):
              shipsPlayer1[currentShipKey]["direction"] = "Up"
              shipsPlayer1[currentShipKey]["image"] = acorazadoUp
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer1[newPosition[1]][newPosition[0]].configure(image=shipsPlayer1[currentShipKey]["image"])"""
            
    currentShipIndex1 += 1 
    element += 1
  element = 0
  #movimiento segundo jugador
  while element < len(shipKeys2):
    currentShipKey = shipKeys2[currentShipIndex2] # En la variable currentShipKey, se guarda el valor de la posición del diccionario que vamos a revisar
    actualPosition = shipsPlayer2[currentShipKey]["position"] # actualPosition, va a almacenar la posición actual de la nave
    newPosition = actualPosition # es la variable que va a almacenar la nueva posición que va a tener la nave
    # Primero, revisamos si la nave aun no ha sido destruida
    if shipsPlayer2[currentShipKey]["alive"] == True: # Creo que esto es descartable, porque para el movimiento no nos importa si está vivo o no, solo si se puede mover
      # Segundo, revisamos si la nave no ha recibido daños y por ende, aún se puede mover
      if shipsPlayer2[currentShipKey]["mobility"] == True:
        # Destructor
        if shipsPlayer2[currentShipKey]["type"] == "Destructor":
          ##Revisión de avance, derecha##
          if shipsPlayer2[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer2[currentShipKey]["position"][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = destructorLeft
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer2[currentShipKey]["position"][0]+1 == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][1]][-1]: 
              newPosition[0] += 1 # x+1
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            else:
              newPosition[0] += 2 # x+2
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]-2].configure(image="")
            """elif checkPositionDestructor(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = destructorLeft
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
            # Si no tiene ninguna limitación"""
            
          ##Revisión de avance, arriba##
          elif shipsPlayer2[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][1] == matrixPlayer2[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = destructorDown
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer2[currentShipKey]["position"][1]-1 == matrixPlayer2[0][0]: 
              newPosition[1] -= 1 # y-1
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]+1][newPosition[0]].configure(image="")
            # Si no tiene ninguna limitación
            else:
              newPosition[1] -= 2 # y-2
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]+2][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = destructorDown
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
          ##Revisión de avance, izquierda##
          elif shipsPlayer2[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer2[currentShipKey]["position"][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = destructorRight
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer2[currentShipKey]["position"][0]-1 == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][1]][0]: 
              newPosition[0] -= 1 # x-1
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]+1].configure(image="")
            # Si no tiene ninguna limitación
            else:  
              newPosition[0] -= 2 # x-2
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]+2].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = destructorRight
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          ##Revisión de avance, abajo##
          elif shipsPlayer2[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][1] == matrixPlayer2[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = destructorUp
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
            # Revisa sí el barco se saldría de la cuadricula al avanzar dos espacios
            elif shipsPlayer2[currentShipKey]["position"][1]+1 == matrixPlayer2[-1][-1]: 
              newPosition[1] += 1 # y-1
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]-1][newPosition[0]].configure(image="")
            # Si no tiene ninguna limitación
            else:  
              newPosition[1] += 2 # y+2
              shipsPlayer2[currentShipKey]["position"] = newPosition
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])
              buttonsMatrixPlayer2[newPosition[1]-2][newPosition[0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif checkPositionDestructor(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = destructorUp
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
        # Crucero
        elif shipsPlayer2[currentShipKey]["type"] == "Crucero":
          ##Revisión de avance, derecha##
          if shipsPlayer2[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer2[currentShipKey]["position"][1][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][1][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = cruceroLeft
              newPosition[0][0] += 1
              newPosition[1][0] -= 1
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroLeft)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroLeft2)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][0] += 1 # trasero x+1
              newPosition[1][0] += 1 # frente x+1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroRight2)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroRight)
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = cruceroLeft
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          ##Revisión de avance, arriba##
          elif shipsPlayer2[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][1][1] == matrixPlayer2[0][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = cruceroDown
              newPosition[0][1] -= 1
              newPosition[1][1] += 1
              
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroDown)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroDown2)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][1] -= 1 # y-1
              newPosition[1][1] -= 1 # y-1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroUp)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroUp2)
              buttonsMatrixPlayer2[newPosition[0][1]+1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = cruceroDown
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          ##Revisión de avance, izquierda##
          elif shipsPlayer2[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer2[currentShipKey]["position"][1][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][0][1]][0]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = cruceroRight
              newPosition[0][0] -= 1
              newPosition[1][0] += 1
              
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroRight)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroRight2)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][0] -= 1 # trasero x-1
              newPosition[1][0] -= 1 # frente x-1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroLeft)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroLeft2)
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]+1].configure(image="")
          ##Revisión de avance, abajo##
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = cruceroRight
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          elif shipsPlayer2[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][1][1] == matrixPlayer2[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = cruceroUp
              newPosition[0][1] += 1
              newPosition[1][1] -= 1
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroUp)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroUp2)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][1] += 1 # y+1
              newPosition[1][1] += 1 # y+1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=cruceroDown2)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=cruceroDown)
              buttonsMatrixPlayer2[newPosition[0][1]-1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = cruceroUp
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
        # Acorazado
        elif shipsPlayer2[currentShipKey]["type"] == "Acorazado":
          ##Revisión de avance, derecha##
          if shipsPlayer2[currentShipKey]["direction"] == "Right":
            # Revisar si se encuentra la borde derecho del tablero
            if shipsPlayer2[currentShipKey]["position"][2][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][2][1]][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = acorazadoLeft
              newPosition[0][0] += 2
              newPosition[2][0] -= 2
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoLeft)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoLeft2)
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoLeft3)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][0] += 1 # trasero x+1
              newPosition[1][0] += 1 # medio x+1
              newPosition[2][0] += 1 # frente x+1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoRight3)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoRight2)
              shipsPlayer2[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoRight)
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]-1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Left"
              shipsPlayer2[currentShipKey]["image"] = acorazadoLeft
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""

          ##Revisión de avance, arriba##
          elif shipsPlayer2[currentShipKey]["direction"] == "Up":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][2][1] == matrixPlayer2[0][0]: #revisa si se encuentra en el borde superior del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = acorazadoDown
              newPosition[0][1] -= 2
              newPosition[2][1] += 2
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoDown)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoDown2)
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoDown3)
            # Si no tiene ninguna limitación
            else:
              newPosition[0][1] -= 1 # y-1
              newPosition[1][1] -= 1 # y-1
              newPosition[2][1] -= 1 # y-1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoUp)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoUp2)
              shipsPlayer2[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoUp3)
              buttonsMatrixPlayer2[newPosition[0][1]+1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Down"
              shipsPlayer2[currentShipKey]["image"] = acorazadoDown
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          ##Revisión de avance, izquierda##
          elif shipsPlayer2[currentShipKey]["direction"] == "Left":
            # Revisar si se encuentra la borde izquierdo del tablero
            if shipsPlayer2[currentShipKey]["position"][2][0] == matrixPlayer2[shipsPlayer2[currentShipKey]["position"][0][1]][0]:
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = acorazadoRight
              newPosition[0][0] -= 2
              newPosition[2][0] += 2
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoRight)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoRight2)
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoRight3)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][0] -= 1 # trasero x-1
              newPosition[1][0] -= 1 # medio x-1
              newPosition[2][0] -= 1 # frente x-1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoLeft)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoLeft2)
              shipsPlayer2[currentShipKey]["position"][2] = newPosition[2]
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoLeft3)
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]+1].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Right"
              shipsPlayer2[currentShipKey]["image"] = acorazadoRight
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""
            
          ##Revisión de avance, abajo##
          elif shipsPlayer2[currentShipKey]["direction"] == "Down":
            # Revisar si se encuentra al borde superior del tablero
            if shipsPlayer2[currentShipKey]["position"][2][1] == matrixPlayer2[-1][-1]: #revisa si se encuentra en el borde derecho del tablero
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = acorazadoUp
              newPosition[0][1] += 2
              newPosition[2][1] -= 2
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoUp)
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoUp2)
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoUp3)
            # Si no tiene ninguna limitación
            else:  
              newPosition[0][1] += 1 # y+1
              newPosition[1][1] += 1 # y+1
              newPosition[2][1] += 1 # y+1
              shipsPlayer2[currentShipKey]["position"][0] = newPosition[0]
              buttonsMatrixPlayer2[newPosition[2][1]][newPosition[2][0]].configure(image=acorazadoDown3)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[1][1]][newPosition[1][0]].configure(image=acorazadoDown2)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[0][1]][newPosition[0][0]].configure(image=acorazadoDown)
              shipsPlayer2[currentShipKey]["position"][1] = newPosition[1]
              buttonsMatrixPlayer2[newPosition[0][1]-1][newPosition[0][0]].configure(image="")
            # Revisa sí el barco puede avanzar uno o dos espacios sin chocar
            """elif duplicatePosition(shipsPlayer2[currentShipKey]["position"]):
              shipsPlayer2[currentShipKey]["direction"] = "Up"
              shipsPlayer2[currentShipKey]["image"] = acorazadoUp
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image="")
              buttonsMatrixPlayer2[newPosition[1]][newPosition[0]].configure(image=shipsPlayer2[currentShipKey]["image"])"""       
    currentShipIndex2 += 1 
    element += 1
    
# Colocar las naves
def actionPlayer1(x,y):
  """La función actionPlayer1 recibe la posición donde se van a colocar las naves del primer jugador y devuelve una imagen para dichas naves

  Args:
      x (int): posición donde se hizo click de la coordenada x
      y (int): posición donde se hizo click de la coordenada y
  """
  global buttonsMatrixPlayer1, matrixPlayer1
  global shipType
  global shipCount
  global shipsPlayer1, currentShipIndex1, shipKeys1
  position = [x,y]
  currentShipKey = shipKeys1[currentShipIndex1] # Posición actual de la nave en el diccionario
  print (f"x={x},y={y}")
  if totalShipsPlayer1 <= 12:  
    if shipType == 1: #destructor
      if rotate == 0:
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 1:
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 2:
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 3:
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=shipsPlayer1[currentShipKey]["image"])
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
    elif shipType == 2: #crucero
      if rotate == 0:
        try:
          buttonsMatrixPlayer1[y][x+1]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y][x+1].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=cruceroRight)
          buttonsMatrixPlayer1[y][x+1].configure(image=cruceroRight2)
          position = [[x,y],[x+1,y]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 1:
        try:
          buttonsMatrixPlayer1[y-11][x]
          if buttonsMatrixPlayer1[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer1[y+1][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer1[y][x].configure(image=cruceroUp)
            buttonsMatrixPlayer1[y-1][x].configure(image=cruceroUp2)
            position = [[x,y],[x,y-1]]
            shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex1 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        
      elif rotate == 2:
        try:
          buttonsMatrixPlayer1[y][x-11]
          if buttonsMatrixPlayer1[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer1[y][x-1].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer1[y][x].configure(image=cruceroLeft)
            buttonsMatrixPlayer1[y][x-1].configure(image=cruceroLeft2)
            position = [[x,y],[x-1,y]]
            shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex1 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        
      elif rotate == 3:
        try:
          buttonsMatrixPlayer1[y+1][x]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y+1][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=cruceroDown)
          buttonsMatrixPlayer1[y+1][x].configure(image=cruceroDown2)
          position = [[x,y],[x,y+1]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
    elif shipType == 3: #acorazado
      if rotate == 0:
        try:
          buttonsMatrixPlayer1[y][x+1] 
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        try:
          buttonsMatrixPlayer1[y][x+2]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y][x+1].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y][x+2].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=acorazadoRight)
          buttonsMatrixPlayer1[y][x+1].configure(image=acorazadoRight2)
          buttonsMatrixPlayer1[y][x+2].configure(image=acorazadoRight3)
          position = [[x,y],[x+1,y],[x+2,y]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 1:
        try:
          buttonsMatrixPlayer1[y-11][x] 
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        try:
          buttonsMatrixPlayer1[y-12][x]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y+1][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y+2][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=acorazadoUp)
          buttonsMatrixPlayer1[y-1][x].configure(image=acorazadoUp2)
          buttonsMatrixPlayer1[y-2][x].configure(image=acorazadoUp3)
          position = [[x,y],[x,y-1],[x,y-2]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 2:
        try:
          buttonsMatrixPlayer1[y][x-11] 
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        try:
          buttonsMatrixPlayer1[y][x-12]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y][x-1].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y][x-2].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=acorazadoLeft)
          buttonsMatrixPlayer1[y][x-1].configure(image=acorazadoLeft2)
          buttonsMatrixPlayer1[y][x-2].configure(image=acorazadoLeft3)
          position = [[x,y],[x-1,y],[x-2,y]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
      elif rotate == 3:
        try:
          buttonsMatrixPlayer1[y+1][x] 
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        try:
          buttonsMatrixPlayer1[y+2][x]
        except IndexError:
          messagebox.showwarning("Advertencia", "El barco no cabe ahí")
        if buttonsMatrixPlayer1[y][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y+1][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        elif buttonsMatrixPlayer1[y+2][x].cget("image") != "":
          messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
        else:
          buttonsMatrixPlayer1[y][x].configure(image=acorazadoDown)
          buttonsMatrixPlayer1[y+1][x].configure(image=acorazadoDown2)
          buttonsMatrixPlayer1[y+2][x].configure(image=acorazadoDown3)
          position = [[x,y],[x,y+1],[x,y+2]]
          shipsPlayer1[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
          currentShipIndex1 += 1
          onClickTrue() # Para volver a habilitar la selección de barcos
    else:
      messagebox.showwarning("Advertencia", "Primero debe de seleccionar un tipo de nave")
  else:
    messagebox.showinfo("Advertencia","El jugador 1 ya colocó todas sus naves")
  # Asignar las cordenadas iniciales al barco
  
def actionPlayer2(x,y):
  """La función actionPlayer2, recibe la posición donde se van a colocar las naves del segundo jugador y devuelve una imagen para dichas naves

  Args:
      x (int): posición donde se hizo click de la coordenada x
      y (int): posición donde se hizo click de la coordenada y
  """
  global buttonsMatrixPlayer2, matrixPlayer2
  global shipType
  global shipCount
  global shipsPlayer2, currentShipIndex2, shipKeys2
  position = [x,y]
  currentShipKey = shipKeys2[currentShipIndex2] # Posición actual de la nave en el diccionario
  print (f"x={x},y={y}")
  if totalShipsPlayer1 <= 12:
    if totalShipsPlayer2 <= 12:  
      if shipType == 1: #destructor
        if rotate == 0:
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=shipsPlayer2[currentShipKey]["image"])
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 1:
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=shipsPlayer2[currentShipKey]["image"])
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 2:
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=shipsPlayer2[currentShipKey]["image"])
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 3:
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=shipsPlayer2[currentShipKey]["image"])
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
      elif shipType == 2: #crucero
        if rotate == 0:
          try:
            buttonsMatrixPlayer2[y][x+1]
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y][x+1].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=cruceroRight)
            buttonsMatrixPlayer2[y][x+1].configure(image=cruceroRight2)
            position = [[x,y],[x+1,y]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 1:
          try:
            buttonsMatrixPlayer2[y-1][x]
          except messagebox.showwarning("Advertencia", "El barco no cabe ahí"):
            print("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y+1][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=cruceroUp)
            buttonsMatrixPlayer2[y-1][x].configure(image=cruceroUp2)
            position = [[x,y],[x,y-1]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 2:
          try:
            buttonsMatrixPlayer2[y][x-1]
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y][x-1].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=cruceroLeft)
            buttonsMatrixPlayer2[y][x-1].configure(image=cruceroLeft2)
            position = [[x,y],[x-1,y]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 3:
          try:
            buttonsMatrixPlayer2[y+1][x]
          except messagebox.showwarning("Advertencia", "El barco no cabe ahí"):
            print("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y+1][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=cruceroDown)
            buttonsMatrixPlayer2[y+1][x].configure(image=cruceroDown2)
            position = [[x,y],[x,y+1]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
      elif shipType == 3: #acorazado
        if rotate == 0: #derecha
          try:
            buttonsMatrixPlayer2[y][x+1] 
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          try:
            buttonsMatrixPlayer2[y][x+2]
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y][x+1].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y][x+2].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=acorazadoRight)
            buttonsMatrixPlayer2[y][x+1].configure(image=acorazadoRight2)
            buttonsMatrixPlayer2[y][x+2].configure(image=acorazadoRight3)
            position = [[x,y],[x+1,y],[x+2,y]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
        elif rotate == 1:#arriba
          try:
            buttonsMatrixPlayer2[y-11][x]
            buttonsMatrixPlayer2[y-12][x]
            if buttonsMatrixPlayer2[y][x].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            elif buttonsMatrixPlayer2[y+1][x].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            elif buttonsMatrixPlayer2[y+2][x].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            else:
              buttonsMatrixPlayer2[y][x].configure(image=acorazadoUp)
              buttonsMatrixPlayer2[y-1][x].configure(image=acorazadoUp2)
              buttonsMatrixPlayer2[y-2][x].configure(image=acorazadoUp3)
              position = [[x,y],[x,y-1],[x,y-2]]
              shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
              currentShipIndex2 += 1
              onClickTrue() # Para volver a habilitar la selección de barcos
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")

        elif rotate == 2:#izquierda
          try:
            buttonsMatrixPlayer2[y][x-11]
            buttonsMatrixPlayer2[y][x-12]
            if buttonsMatrixPlayer2[y][x].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            elif buttonsMatrixPlayer2[y][x-1].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            elif buttonsMatrixPlayer2[y][x-2].cget("image") != "":
              messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
            else:
              buttonsMatrixPlayer2[y][x].configure(image=acorazadoLeft)
              buttonsMatrixPlayer2[y][x-1].configure(image=acorazadoLeft2)
              buttonsMatrixPlayer2[y][x-2].configure(image=acorazadoLeft3)
              position = [[x,y],[x-1,y],[x-2,y]]
              shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
              currentShipIndex2 += 1
              onClickTrue() # Para volver a habilitar la selección de barcos
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")

        elif rotate == 3:#abajo
          try:
            buttonsMatrixPlayer2[y+1][x] 
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          try:
            buttonsMatrixPlayer2[y+2][x]
          except IndexError:
            messagebox.showwarning("Advertencia", "El barco no cabe ahí")
          if buttonsMatrixPlayer2[y][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y+1][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          elif buttonsMatrixPlayer2[y+2][x].cget("image") != "":
            messagebox.showwarning("Advertencia", "Ya hay otro barco en ese sitio")
          else:
            buttonsMatrixPlayer2[y][x].configure(image=acorazadoDown)
            buttonsMatrixPlayer2[y+1][x].configure(image=acorazadoDown2)
            buttonsMatrixPlayer2[y+2][x].configure(image=acorazadoDown3)
            position = [[x,y],[x,y+1],[x,y+2]]
            shipsPlayer2[currentShipKey]["position"] = position # Se le asigna su posición en el tablero
            currentShipIndex2 += 1
            onClickTrue() # Para volver a habilitar la selección de barcos
      else:
        messagebox.showwarning("Advertencia", "Primero debe de seleccionar un tipo de nave")
    else:
      messagebox.showinfo("Advertencia","El jugador 2 ya colocó todas sus naves")
  else:
    messagebox.showwarning("Advertencia", "El jugador 1 todavía no termina de colocar sus naves")

# Generación del tablero
def board(x: int, y: int) -> Tk:
  global buttonsMatrixPlayer1, buttonsMatrixPlayer2, matrixPlayer1, matrixPlayer2
  global currentShipIndex1
  global windowHeight, windowWidth
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
        btn.place(x=posx, y=posy, height = buttonHeight, width = buttonWidth)
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

def textOutput(game,family,size,color):
  global windowHeight, windowWidth
  global actualText
  # Crear un Label para mostrar el texto
  labelWidth = int((windowWidth )) # X
  labelHeight = int((windowHeight)) # Y
  center = (windowWidth - labelWidth) // 4.2
  label = Label(game, text=actualText, bg="lightblue", fg="black", width=labelWidth, height=labelHeight, borderwidth=10, relief="solid")
  def updateFont(family, size, color):
    # Crear una nueva fuente
    newFont = Font(family=family, size=size)
    # Aplicar la nueva fuente y el color al Label
    label.config(font=newFont, fg=color)
  # Ejemplo de uso de la función update_font
  updateFont(family, size, color)
  # Posicionar el Label
  label.place(x=center,y=20)

game = board(boardColumns(),boardRows())
#textLabel = textOutput(game,family,size,color)

##KeyBinds##
game.bind("<KeyPress-q>", lambda event : selectShip1(event))
game.bind("<KeyPress-w>", lambda event : selectShip2(event))
game.bind("<KeyPress-e>", lambda event : selectShip3(event))
on_press_key("r", rotateShip)

# Iniciar el juego
game.bind("<KeyPress-t>", lambda event : shipMovement(event))

game.mainloop()