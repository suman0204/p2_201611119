def sumList(aList):
    x=list()
    for i in range(0,aList):
        if i%4==0 and not i%5==0:
            x.append(i)
            
    mysum=0
    
    for i in range(0,len(x)):
        mysum+=x[i]
    return mysum


def lab6():
  
    print """w6 p2 201611119 homework"""
    aList=1000
    labsum=sumList(aList)
    print labsum
    
def main():
    lab6()

main()