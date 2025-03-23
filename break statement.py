#program will demonstrate break statement

i=1
sum=0
ans="y"
while ans=="y":
    x1=float(input('enter a number: '))
    if x1<0:
        print("enter number greater than zero!")
        break
    sum+=x1
    i+=1
    ans=input("want to enter more numbers?(y/n)....")
else:
    print("sum is:",sum)
        