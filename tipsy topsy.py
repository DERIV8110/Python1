x1=float(input('enter a number: '))
if x1>20:
    if (x1%3==0)==True and (x1%7==0)==False:
        print('tipsy')
    elif (x1%3==0)==False and (x1%7==0)==True:
        print('topsy')
    elif (x1%3==0)==True and (x1%7==0)==True:
        print('tipsy topsy')
    else:
        print('neither multiple of 3 nor 7')
else:
    print('enter no. greater than 20')