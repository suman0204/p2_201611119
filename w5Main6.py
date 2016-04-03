def Game():
    print "Let's play R S P game!!"
    p1=raw_input("userA: ")
    p2=raw_input("userB: ")
    def number(user):
        if(user=='Rock'):
            return 2.0
        elif(user=='Scissors'):
            return 4.0
        elif(user=='Paper'):
            return 8.0
        else:
            print "Input Error"   

    s=number(p1)/number(p2)
    if(s==0.5):
        print "userA wins"
    elif(s==1.0):
        print "draw"
    elif(s==0.25):
        print "userB wins"
    elif(s==2.0):
        print "userB wins"
    elif(s==4.0):
        print "userA wins"
Game()
