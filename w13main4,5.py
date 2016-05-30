import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import os
mydir=os.getcwd()


def assignment1():
    try:
        fin1=open('python.txt','a')
        fin2=open('outputNumber.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
        



def getCoordsFromFile(aFile):
    frec=open(aFile)
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
    frec.close()
    return mycoords


def drawSquareWithCoords(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        print x1,y1,x2,y2
        t1.penup()
        t1.goto(x1,y1)
        t1.pendown()
        for i in range(0,4):
            t1.fd(x1-x2)
            t1.right(90)

def lab13():
    assignment1()
    aFile='reccoords.txt'
    getCoordsFromFile(aFile)
    mycoords= getCoordsFromFile(aFile)
    drawSquareWithCoords(mycoords)


def main():
    lab13() 
    wn.exitonclick()
               
               
if __name__=="__main__":
        main()