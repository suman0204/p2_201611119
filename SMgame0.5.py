import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.goto(0,-150)
t1.setheading(90)
t1.shape("turtle")
t2.speed(10)
t2.penup()


t2.goto(-350,100)
for i in range(0,3):
    t2.pendown()
    t2.fd(100)
    t2.right(120)
t2.penup()
t2.goto(-50,100)
for i in range(0,5):
    t2.pendown()
    t2.fd(100)
    t2.right(72)
t2.penup()
t2.goto(200,100)
for i in range(0,5):
    t2.pendown()
    t2.fd(100)
    t2.right(144)
t2.pendown()


angle=45
def fd():
    t1.fd(10)
def back():
    t1.back(10)
    
def right():
    t1.right(angle)
def left():
    t1.left(angle)

wn.onkey(fd,"Up")
wn.onkey(back,"Down")
wn.onkey(right,"Right")
wn.onkey(left,"Left")
wn.listen()
stopper = 0
t1.speed=5
