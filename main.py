from tkinter import *
from boardDimensions import * #llamada al archivo boardDimensions
from PIL import ImageTk, Image

buttonsMatrix=[]

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

game=board(boardColumns(),boardRows())

shipImage = Image.open("b1.png")
shipImage = shipImage.resize((50, 50))  # Ajusta el tamaño de la shipImage
shipImageRotated = shipImage.rotate(90)
shipImage = ImageTk.PhotoImage(shipImageRotated)
game.mainloop()