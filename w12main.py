import os
mydir=os.getcwd()

def assignment1():
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    try:
        myfile=open(myfilename,'r')
        contents=myfile.readlines()
        for line in range(0,len(contents)):
            if contents[line].find('Python')>=0:
                print contents[line]
        myfile.close()
    except IOError as e:
        print e


def assignment2():
    myfile2=open('output.txt','w')
    line1='first line\n'
    myfile2.write(line1)
    line2='\tsecond line\n'
    myfile2.write(line2)
    line3='thirdline'
    myfile2.write(line3)
    myfile2.close()
    myfile2=open('output.txt','r')
    for c in myfile2:
        s='line'
        if c.find('line') >=0:
            print s.upper()
    myfile2.close()



def lab12():
    print "Assignment1"
    assignment1()
    print "Assignment2"
    assignment2()
    
    
def main():
    lab12()
    raw_input()
    
if __name__=="__main__":
    main()

