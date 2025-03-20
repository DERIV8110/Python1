temp=float(input('enter the temperature> '))
if temp<-273.15:
    print("below absolute zero, invalid")
if temp==-273.15:
    print("absolute zero, invalid")
if -273.15<temp<0:
    print("below freezing")
if temp==0:
    print("at freezing point")
if 0<temp<100:
    print("at normal range")
if temp==100:
    print('at boiling point')
if temp>100:
    print('above boiling point')