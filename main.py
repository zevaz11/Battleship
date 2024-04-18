from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

buttonsMatrix=[]
rotate = 0
##Variables de los barcos##
#acorazado
destructorRight = Image.open("b1.png")
destructorUp = Image.open("b1.png")
destructorUp = destructorUp.rotate(90)
destructorLeft = Image.open("b1.png")
destructorLeft = destructorLeft.rotate(180)
destructorDown = Image.open("b1.png")
destructorDown = destructorDown.rotate(270)

shipType = 1

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
def action(x,y):
  global buttonsMatrix
  global shipType
  print (f"x={x},y={y}")
  if shipType == 1: #destructor
    if rotate == 0:
      buttonsMatrix[y][x].configure(image=destructorRight)
    elif rotate == 1:
      buttonsMatrix[y][x].configure(image=destructorUp)
    elif rotate == 2:
      buttonsMatrix[y][x].configure(image=destructorLeft)
    elif rotate == 3:
      buttonsMatrix[y][x].configure(image=destructorDown)
  elif shipType == 2: #crucero
    if rotate == 0:
      buttonsMatrix[y][x].configure(image=cruceroRight)
    elif rotate == 1:
      buttonsMatrix[y][x].configure(image=cruceroUp)
    elif rotate == 2:
      buttonsMatrix[y][x].configure(image=cruceroLeft)
    elif rotate == 3:
      buttonsMatrix[y][x].configure(image=cruceroDown)
  elif shipType == 3: #acorazado
    if rotate == 0:
      buttonsMatrix[y][x].configure(image=acorazadoRight)
    elif rotate == 1:
      buttonsMatrix[y][x].configure(image=acorazadoUp)
    elif rotate == 2:
      buttonsMatrix[y][x].configure(image=acorazadoLeft)
    elif rotate == 3:
      buttonsMatrix[y][x].configure(image=acorazadoDown)
 
def board (x:int,y:int)->Tk:
  global buttonsMatrix 
  game = Tk()
  game.title("Piratas de Golfito")
  game.state("zoomed")
  resolucion=f"{x*50}x{y*50}+0+0"

  game.geometry(resolucion)

  buttonsMatrix=[[Button(game, command=lambda x=c,y=f:action(x,y)) for c in range(x)] for f in range(y)]
  posx=0
  posy=0
  for buttonsRow in buttonsMatrix:
    posx=0
    for btn in buttonsRow:
      btn.place(x=posx,y=posy,height=50, width=50)
      btn.configure(bg = "#47A9CC")
      posx+=50
    posy+=50
  return game

game = board(boardColumns(),boardRows())

##KeyBinds##
shipImage = game.bind("<KeyPress-q>", lambda event : selectShip1(event))
shipImage = game.bind("<KeyPress-w>", lambda event : selectShip2(event))
shipImage = game.bind("<KeyPress-e>", lambda event : selectShip3(event))
on_press_key("r", rotateShip)

game.mainloop()