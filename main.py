from tkinter import *
from keyboard import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

buttonsMatrix=[]
count = 0

##Funciones KeyBinds##
def rotateShip(event):
  global count
  if event.name == 'r' and event.event_type == KEY_DOWN:
    count += 1
  if count > 3:
    count = 0
  return count
on_press_key("r", rotateShip) #// revisar porque no funciona.

def selectShip1(event):
  global shipImage
  global count 
  shipImage = Image.open("b1.png")
  shipImage = shipImage.resize((50, 50))
  shipImageRotated = shipImage.rotate(90*count)
  shipImage = ImageTk.PhotoImage(shipImageRotated)
  print("Seleccionaste el destructor")
  return shipImage

def selectShip2(event):
  global shipImage
  global count 
  shipImage = Image.open("b22.png")
  shipImage = shipImage.resize((50, 50))
  shipImageRotated = shipImage.rotate(90*count)
  shipImage = ImageTk.PhotoImage(shipImageRotated)
  print("Seleccionaste el barco grande")
  return shipImage

def selectShip3(event):
  global shipImage 
  global count 
  shipImage = Image.open("b33.png")
  shipImage = shipImage.resize((50, 50))
  shipImageRotated = shipImage.rotate(90*count)
  shipImage = ImageTk.PhotoImage(shipImageRotated)
  print("Seleccionaste el barco aún mas grande")
  return shipImage

# Colocar las naves //aun no se como funciona esta cosa
def action(x,y):
  print (f"x={x},y={y}")
  global buttonsMatrix
  global shipImage
  buttonsMatrix[y][x].configure(image=shipImage)
 
def board (x:int,y:int)->Tk:
  global buttonsMatrix 
  game = Tk()
  game.title("Piratas de Golfito")
  resolucion=f"{x*50}x{y*50}+0+0"
  game.geometry(resolucion)
  buttonsMatrix=[[Button(game, command=lambda x=c,y=f:action(x,y)) 
                   for c in range(x)] for f in range(y)]
  posx=0
  posy=0
  for buttonsRow in buttonsMatrix:
    posx=0
    for btn in buttonsRow:
      btn.place(x=posx,y=posy)
      btn.configure(height=50, width=50)
      posx+=50
    posy+=50
  return game

game = board(boardColumns(),boardRows())

##KeyBinds##
shipImage = game.bind("<KeyPress-q>", lambda event : selectShip1(event))
shipImage = game.bind("<KeyPress-w>", lambda event : selectShip2(event))
shipImage = game.bind("<KeyPress-e>", lambda event : selectShip3(event))

game.mainloop()