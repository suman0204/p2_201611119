height=input ("input user height (m) : ")
weight=input ("input user weight (kg): ")
print "%s" %height, "%s" %weight
BMI=weight/(height*height)
print "%s" %BMI
if BMI<18.5:
     print 'Low weight'
elif 18.5<= BMI <23:
     print 'normal weight'

elif 23<= BMI <25:
       print 'over weight'
else:
    print 'very over weight'