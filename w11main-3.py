import turtle
wn=turtle.Screen()
wn.bgpic("C:\Users\P400\Desktop/myMaze.gif")
t1=turtle.Turtle()
t1.shape("turtle")
t1.speed(1)
t1.penup()
t1.goto(-320,300)
t1.clear()
t1.pendown()

def keyup():
     t1.fd(50)
def keydown():
     t1.back(50)
def keyright():
     t1.right(45)
def keyleft():
     t1.left(45)
def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
def mousegoto(x,y):
     t1.setpos(x,y)
        
def addmouse():
     wn.onclick(mousegoto)


addkeys()
addmouse()
wn.listen()
turtle.mainloop()
