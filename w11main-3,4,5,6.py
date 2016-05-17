import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("C:\Users\Administrator\Desktop\myMaze.gif")
import math
line1=[(50,250),(150,250)]
x1=line1[0][0]-10
y1=line1[0][1]-10
x2=line1[1][0]+10
y2=line1[1][1]+10
pos1=(x1,y1)
pos2=(x2,y2)




def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye
def BlureRectangle((x,y),size):
    angle = 90
    t1.fillcolor("blue")
    t1.begin_fill()
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
    t1.end_fill()

def Rectangle((x,y),size):
    angle = 90
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
        
def isInCircle(center,radius,pos):
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius

def drawcircle((x,y),size):
    t1.setpos(x,y)
    t1.setheading(0)
    t1.fillcolor("red")
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
    
    
def drawLine():
    t1.setheading(0)
    t1.penup()
    t1.goto(50,250)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.goto(-315,330)
    
    
def isOnLine(curpos,pos1,pos2):
    if x1<=curpos[0]<=x2 and y1<=curpos[1]<=y2:
        t1.color("yellow")
        drawLine()


def base():
    t1.clear()
    t1.setpos(100,0)
    t1.circle(100)
    Rectangle((0,0),100)
    drawLine()
    

def keyup():
    pos=t1.pos()
    t1.forward(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        BlueRectangle((0,0),100)
    if isInCircle((100,100),100,pos):
        drawcircle((100,0),100)
    isOnLine(pos,pos1,pos2)

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
        drawcircle((100,0),100)
    isOnLine(pos,pos1,pos2)

    
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
        drawcircle((100,0),100)
    isOnLine(pos,pos1,pos2)


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