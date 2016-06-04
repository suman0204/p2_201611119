import turtle
import random
import time
import math
b1=turtle.Turtle()
p1=turtle.Turtle()
s1=turtle.Turtle()
gover=turtle.Turtle()
x1=turtle.Turtle()
y1=turtle.Turtle()
wn=turtle.Screen()
def ScreenBoundary():
    wn.setup(700, 700)
    wn.bgcolor("Black")
      
    b1.pencolor("Green")
    b1.penup()
    b1.goto(-300, -300)
    b1.pendown()

    for i in range(4):
        b1.ht()
        b1.fd(600)
        b1.lt(90)


def player():
    p1.shape("turtle")
    p1.color("Pink")
    p1.penup()
    p1.width(4)


def square():
    s1.shape("square")
    s1.color("Yellow")
    s1.penup()
    s1.speed(0)
    s1.goto(-100, 100)


def up():
    p1.setheading(90)

def down():
    p1.setheading(270)

def left():
    p1.setheading(180)

def right():
    p1.setheading(0)

def addkeys():        
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(up, "Up")
    wn.onkey(down, "Down")
    wn.listen()

    
   


def gameOver():
    gover.ht()
    gover.pencolor("Red")
    gover.write("GAME OVER!", align = "center", font = ("",20,"bold"))

       




        

    
def recordScore():
    playedscore = open("record.txt",'a')
    if p1.xcor() < -300 or p1.xcor() > 300:
        name = raw_input("Input in your name: ")
        msg='playscore {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print "End Game"+'\n'+'Score' + '\t'+ str(pScore) +'\t' + msg
        playedscore.write('\n' + 'Score' + '\t'+ str(pScore) +'\t' + msg)
        playedscore.close()
        wn.exitonclick()
    elif p1.ycor() < -300 or p1.ycor() > 300:
        name = raw_input("Input in your name: ")
        msg='playscore {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print "End Game"+'\n'+'Score' + '\t'+ str(pScore) +'\t' + msg
        playedscore.write('\n' + 'Score' + '\t'+ str(pScore) +'\t' + msg)
        playedscore.close()
        wn.exitonclick()
  
    
           


def TurtleGame():
    ScreenBoundary()
    player()
    square()
    addkeys()
    recordScore()
    score=0
    speed=2
    while True:
        
        p1.fd(speed)

        if p1.xcor() < -300 or p1.xcor() > 300:
            gameOver()
            p1.ht()
            pScore = "Score = " + str(score)
            x1.ht()
            x1.goto(0, -100)
            x1.pencolor("Red")
            x1.write(pScore, align = "center", font = ("", 15, "bold"))

        elif p1.ycor() < -300 or p1.ycor() > 300:
            gameOver()
            p1.ht()
            pScore = "Score = " + str(score)
            y1.ht()
            y1.goto(0, -100)
            y1.pencolor("Red")
            y1.write(pScore, align = "center", font = ("", 15, "bold"))

                  
        r1 = s1.xcor() + 15
        r2 = s1.xcor() - 15
        r3 = s1.ycor() + 15
        r4 = s1.ycor() - 15
        if (p1.xcor() >= r2 and p1.xcor() <= r1) and (p1.ycor() >= r4 and p1.ycor() <= r3):
            s1.goto(random.randint(-290, 290), random.randint(-290, 290))
            score += 1
            speed += 1

TurtleGame()
turtle.mainloop()