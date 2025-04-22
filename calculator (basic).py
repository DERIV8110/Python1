x1=float(input('enter number: '))
x2=float(input('enter number: '))
opr=input("enter operation you want: ")
if len(opr)>=2:
    print("enter a single operation")
else:
    if opr=="+":
        print(x1+x2)
    elif opr=="-":
        print(x1-x2)
    elif opr=="*":
        print(x1*x2)
    elif opr=="/":
        print(x1/x2)