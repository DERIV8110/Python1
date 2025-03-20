print("enter five numbers below")
x1=float(input('enter first number: '))
x2=float(input('enter second number: '))
x3=float(input('enter third number: '))
x4=float(input('enter fourth number: '))
x5=float(input('enter fifth number: '))
divisor=float(input('enter divisor: '))
if x1%divisor==0:
    print(divisor, "divides first number")
if x2%divisor==0:
    print(divisor, "divides second number")
if x3%divisor==0:
    print(divisor, "divides third number")
if x4%divisor==0:
    print(divisor, "divides fourth number")
if x5%divisor==0:
    print(divisor, "divides fifth number")
else:
    print("none numbers are divisble by",divisor)