import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import math
    


def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye
def BlueRectangle((x,y),size):
    angle = 90
    t1.fillcolor("blue")
    t1.begin_fill()
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
    t1.end_fill()

def Rectnagle((x,y),size):
    angle = 90
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
        

def drawcircle((x,y),size):
    t1.setpos(x,y)
    t1.setheading(0)
    t1.fillcolor("red")
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
    
def base():
    t1.clear()
    t1.setpos(100,0)
    t1.circle(100)
    Rectangle((0,0),100)



def keyup():
    pos=t1.pos()
    t1.forward(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        BlueRectangle((0,0),100)
    if isInCircle((100,100),100,pos):
        drawcircle((100,0),100)
   
        
def keyleft():
    t1.left(45)
    
def keyright():
    t1.right(45)

def keydown():
    pos=t1.pos()
    t1.back(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        BlueRectangle((0,0),100)
    if isInCircle((100,100),100,pos):
        circle((100,0),100)
 
    
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
     
def mousegoto(x,y):
    t1.setpos(x,y)
    pos=t1.pos()
    if isInRectangle((x,y),[(0,-100),(100,0)]):
        BlueRectangle((0,0),100)
    if isInCircle((100,100),100,pos):
        circle((100,0),100)
def addMouse():
    wn.onclick(mousegoto)
    
def gamePlay():
    base()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()


def lab11():
    gamePlay()

lab11()