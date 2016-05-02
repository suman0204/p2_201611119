def charCount(word):
    global d
    d=dict()
    for c in sentence:
        if c not in d:
            d[c]=1
            print d
        else:
            d[c]=d[c]+1
    return d
    
def drawBar():
    
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()
    
def lab8():
    global word
    word='sangmyung university'
    result=charCount(word)
    print result
    drawBar()
    
def main():
    lab8()
    
if__name__=="__main__":
    main()			