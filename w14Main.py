class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ",self.name
    def talk(self):
        print "mung mung"
        
class ShihTzuDog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ",self.name
    def talk(self):
        print "si si"

class Maltese(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ",self.name
    def talk(self):
        print "mal mal"
        
def dogSound():
    mydog=Dog('poppy')
    mydog.getName()
    mydog.talk()
    Shi=ShihTzuDog('ShihTzu')
    Shi.getName()
    Shi.talk()
    Mal=Maltese('Maltese')
    Mal.getName()
    Mal.talk()
    
def lab14():
    dogSound()

def main():
    lab14()
    
if __name__=="__main__":
    main()