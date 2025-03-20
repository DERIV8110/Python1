x1=float(input('enter first number: '))
x2=float(input('enter second number: '))
if 0<abs(x1-x2)<=0.001:
    print(x1, x2, "Close")
else:
    print("not close")
#this code works for N,Z