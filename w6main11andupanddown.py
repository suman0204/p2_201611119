

def yunyear():
    year=input ("input year : ")
    if year%4==0 and not year%100==0:
        result = "yun year"
    elif year%4==0 and year%400==0:
        result = "yun year"
    else:
        result = "not yun year"
    print result
    





def upanddown():
    import random
    number=raw_input("input range number 1~N : ")
    s2=int(number)
    r1=random.randrange(1,s2+1)
    print "Number's range is 1~%f" %s2
    def subtool():
        selectN=raw_input("input number you want: ")
        s1=int(selectN)
        global s1
    def maintool():
        if(s1==r1):
            print "correct!"
        else:
            if(s1>r1):
                print "down"
                subtool()
                maintool()
            elif(s1<r1):
                print "up"
                subtool()
                maintool()
            else:
                print "Error"
    subtool()
    maintool()
    


def lab6():
      yunyear()
      upanddown()
      
def main():
      lab6()
      

if __name__=="__main__" :
       main()