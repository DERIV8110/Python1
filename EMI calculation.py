p=float(input('enter principal loan amt: '))
r=float(input('enter rate of interest: '))/100
n=float(input('enter tenure of loan repayment in months: '))

e=(p*r*((1+r)**n))/(((1+r)**n)-1)

print("EMI:",e)