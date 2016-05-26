import time
def assignment1():
    myfile=open('output.txt','w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third line'
    myfile.write(line3)
    myfile.close()
    msg='[hsm edited {0}]'.format(time.strftime('%Y.%m.%d  %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for word in words:
            if word == 'line':
                fout.write('\t')    
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
    

def assignment2():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber2.txt','w')
    for i in data:
        print "{0}\t".format(i)
        fout.write(str)
        if i%2==0:
        fout.write('\n')
    fout.close()
    
    
def lab12():
    assignment1()
    assignment2()

def main():
    lab12()
    raw_input()