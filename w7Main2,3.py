import turtle
t1=turtle.Turtle()
wn=turtle.Screen()


def drawSquareAtSave(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks


def drawSquareForm(tracks):
    tracks=dict()
    tracks=({0:(0,0),1:(100,0),2:(100,100),3:(0,100),4:(0,0)})

    for i in range(1,5):
        t1.goto(tracks[i])
    for j in range(1,5):
        print tracks[j]



def lab7b():
    mytrack=drawSquareAt(size,pos)
    print mytracks

def lab7c():
    drawSquareForm(tracks)
    

    
    
def main():
    lab7b()
    lab7c()
    
if __name__== "__main__":
       main()
    
wn.exitonclick()

main()

wn.exitonclick()