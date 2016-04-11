def sumList(x):
    x=list()
    for i in range(1,1000):
        if i%4==0 and not i%5==0:
            x.append(i)
            
    sum=0
    
    for i in range(0,len(x)):
        sum+=x[i]
    return sum
print sum


def lab6():
    print """w6 p2 201611119 homework"""
    labsum=sumList(x)
    print labsum
    
def main():
    lab6()
    


main()