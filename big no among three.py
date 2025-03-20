num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
num3=int(input('enter third number: '))
if num1>num2 and num1>num3:
    print('first entered no. is big among all')
if num2>num3 and num2>num1:
    print('second entered no. is big among all')
if num3>num2 and num3>num1:
    print('third entered no. is big among all')
    #checking if lengths are equal
if num1>num2 and num1==num3:
    print('first entered no. is bigger than second and equal to third.')
if num1==num2 and num1>num3:
    print('first entered no. is bigger than third and equal to second.')
if num2>num3 and num2==num1:
    print('second entered no. is bigger than third and equal to first.')
if num2==num3 and num2>num1:
    print('second entered no. is bigger than first and equal to third.')
if num3>num2 and num3==num1:
    print('third entered no. is bigger than second and equal to first.')
if num3==num2 and num3>num1:
    print('third entered no. is bigger than first and equal to second.')
if num3==num2 and num3==num1 and num1==num2:
    print('all equal daddy 😋😊')


    