#sum1 as the sum of all input numbers
#sum2 as the sum of non-duplicate numbers; 
# if there are duplicate numbers in the input, ignore them.
sum1=sum2=0
x1=float(input('enter first number: '))
x2=float(input('enter second number: '))
x3=float(input('enter third number: '))
sum1=x1+x2+x3
if x1==x2:
    if x3!=x1:
        sum2+=x3 #agar x1 x2 ke barabar hai aur x3 x1 ke equal nahi hai 
                 #toh sum2 (jo zero ke equal hai initialy), 
                 # usme x3 ka value add karke zero replace kardo (sum2+=x3)
if x2==x3:
    if x1!=x2:
        sum2+=x1
if x3==x1:
    if x2!=x1:
        sum1+=x2
else:
    print("numbers are ", x1, x2, x3)
    print("sum of these given numbers is ", sum1)
    print("sum of non-duplicate number is ", sum2)

