n=float(input('enter dividend(n)> '))
m=float(input('enter divisor(m)> '))
if n%m==0:
    print(n,"is divisible by",m)
    if n%2==0:
        print(n,"is an even number")
    else:
        print(n,"odd number")
else:
    print(n,"is not divisible by",m)
    if n%2==0:
        print(n,"is an even number")
    else:
        print(n,"is an odd number")