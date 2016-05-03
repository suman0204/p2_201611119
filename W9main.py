import matplotlib
import matplotlib.pyplot as plt


def charCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
            print d
        else:
            d[c]=d[c]+1
    print d
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()



def countDigitsLetter(word):
    d=dict()
    d={"number":0, "word":0}
    for c in word:
        if c.isdigit()==True:
            d["number"]+=1
        elif c.isdigit()==False:
            d["word"]+=1
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()




def myroomfriendroom():
    myroom=set()
    friendroom=set()
    myroom={'TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recorder'}
    friendroom={'coffee machine','radio','camera','running machine','ramp','computer','notebook','recorder'}
    print myroom
    print friendroom
    onlymyroom=myroom.difference(friendroom)
    print onlymyroom
    onlyfriendroom=friendroom.difference(myroom)
    print onlyfriendroom
    union=myroom.union(friendroom)
    print union
    intersection=myroom.intersection(friendroom)
    print intersection


    d=dict()
    for c in myroom:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    for c in friendroom:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
            
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()




def lab9_1():
    word='sangmyung university'
    charCount(word)



def lab9_2():
    word="7 hongjidong"
    countDigitsLetter(word)


def lab9_3():
    myroomfriendroom()

def main():
    lab9_1()
    lab9_2()
    lab9_3()


if __name__=="__main__":
    main()