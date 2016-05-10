def Coffee():
    alldata=list()
    alldata=[["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes","No"],
    ["Affogato","No","No","Yes"]]

    for i in range(1,len(alldata)):
            print alldata[i]
    data=alldata[1:]
    milk=0
    for c in data:
        if c[2]=="Yes":
            milk+=1
    milk=float(milk)
    percent=str(milk/5*100)
    print "Milk's percent is"+percent+"%"



def Grades():
    marks=list()
    marks=[["English",100],["Math",200],["English", 200],["Math", 200],["English", 100],["Math",300]]
    EnglishSum=0
    MathSum=0
    en=0
    ma=0
    for i in range(0,len(marks)):
        if marks[i][0]=="English":
            EnglishSum=EnglishSum+marks[i][1]
    for i in range(0,len(marks)):
        if marks[i][0]=="Math":
            MathSum=MathSum+marks[i][1]

    for i in marks:
            if i[0]=="English":
                en+=1
            elif i[0]=="Math":
                ma+=1
    print "EnglishSum is ",EnglishSum ,"MathSum is ",MathSum
    print "English average is ",EnglishSum/en,"Math average is " ,MathSum/ma



def LetItBe():
    lyrics=list()
    lyrics=["when I find myself in times of trouble", 
    "mother Mary comes to me", 
    "speaking words of wisdom let it be", 
    "and in my hour of darkness", 
    "she is standing right in front of me" ,
    "speaking words of wisdom let it be ",
    "let it be let it be let it be let it be" ,
    "whisper words of wisdom let it be ",

    "and when the broken hearted people ",
    "living in the world agree ",
    "there will be an answer let it be" ,
    "for though they may be parted" ,
    "there is still a chance that they will see" ,
    "there will be an answer let it be",
    "let it be let it be let it be let it be ",
    "there will be an answer let it be ",
    "let it be let it be let it be let it be ",
    "whisper words of wisdom, let it be ",
    "let it be let it be let it be let it be ",
    "whisper words of wisdom let it be",

    "and when the night is cloudy ",
    "there is still a light that shines on me ",
    "shine until tomorrow let it be ",
    "i wake up to the sound of music ",
    "mother Mary comes to me ",
    "speaking words of wisdom let it be",
    "let it be let it be let it be, let it be",
    "there will be an answer let it be",
    "let it be, let it be let it be let it be" ,
    "whisper words of wisdom let it be"]

    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    print d
    for h in range(len(d)):
        if d.values()[h]>=20:
            print d.keys()[h],d.values()[h]


def lab10():
    Coffee()
    Grades()
    LetItBe()
def main():
    lab10()
main()

if __name__=="__main__":
    main()
    
wn=raw_input()