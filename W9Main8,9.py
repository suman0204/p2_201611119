kbg=(37.5758422,126.9713913)
kwm=(37.5716232,126.9742473)
ak=(37.5765602,126.9832833)
jk=(37.5701732,126.9809103)
jr=(37.5704272,126.9899833)
sch=(37.5657079,126.9746729)

Locations=tuple()
Locations=(kbg,kwm,ak,jk,jr,sch)


import math

mylist=list()
for i in Locations:
    distance=math.sqrt((kbg[0]-i[0])**2+(kbg[1]-i[1])**2)
    mylist.append(distance)
    print 'distance',distance
mylist.remove(0)
print 'short distance is',min(mylist)




population=[(74425,76326),
            (61164,61636),
            (109688,115744),
            (144796,146776),
            (174996,181676),
            (177841,177434),
            (204630,205980),
            (223373, 232245),
            (161055 ,166130),
            (171576 ,176735),
            (279169 ,293772),
            (239450 ,251066),
            (148690, 156510),
            (182977, 196992),
            (237792 ,242641),
            (283869, 296762),
            (209344, 210282),
            (118965 ,114441),
            (186503 ,186856),
            (195734 ,203014),
            (254381, 249472),
            (212401, 229111),
            (271654, 295354),
            (319197, 335045),
            (229829, 231671)]



mansum=0
for i in population:
    mansum=mansum+i[0]
print mansum


womansum=0
for i in population:
    womansum=womansum+i[1]
print womansum


manaver=mansum/len(population)
print manaver


womanaver=womansum/len(population)
print womanaver


man=mansum
woman=womansum
manaver=manaver
womanaver=womanaver

x=dict()
x={"mansum":man,"womansum":woman,"manaver":manaver,"womanaver":womanaver}

import matplotlib 
import matplotlib.pyplot as plt
plt.bar(range(len(x)),x.values(), align='center')
plt.xticks(range(0,10), list(x.keys()))
plt.show()

gusum=list()
for a in population:
    gusum.append(a[0]+a[1])
print gusum


plt.bar(range(len(gusum)),gusum,align='center')
plt.show()