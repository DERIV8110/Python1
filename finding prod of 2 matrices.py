order=int(input("enter order of matrix(2 or 3): "))
if order==2:
       print("AxB=C, where A,B and C are 2x2 Matrices.")
       a=int(input("enter element a11 of A: "))
       b=int(input("enter element a12 of A: "))
       c=int(input("enter element a21 of A: "))
       d=int(input("enter element a22 of A: "))

       e=int(input("enter element a11 of B: "))
       f=int(input("enter element a12 of B: "))
       g=int(input("enter element a21 of B: "))
       h=int(input("enter element a22 of B: "))

       a11=a*e+b*g
       a12=a*f+b*h
       a21=c*e+d*g
       a22=c*f+d*h

       print(a11,a12,"\n\n",a21,a22)
else:
       print("AxB=C, where A,B and C are 3x3 Matrices.")
       a=int(input("enter element a11 of A: "))
       b=int(input("enter element a12 of A: "))
       c=int(input("enter element a13 of A: "))
       d=int(input("enter element a21 of A: "))
       e=int(input("enter element a22 of A: "))
       f=int(input("enter element a23 of A: "))
       g=int(input("enter element a31 of A: "))
       h=int(input("enter element a32 of A: "))
       i=int(input("enter element a33 of A: "))
       j=int(input("enter element a11 of B: "))
       k=int(input("enter element a12 of B: "))
       l=int(input("enter element a13 of B: "))
       m=int(input("enter element a21 of B: "))
       n=int(input("enter element a22 of B: "))
       o=int(input("enter element a23 of B: "))
       p=int(input("enter element a31 of B: "))
       q=int(input("enter element a32 of B: "))
       r=int(input("enter element a33 of B: "))
       a11=a*j+b*m+p*c
       a12=a*k+b*n+c*q
       a13=a*l+b*o+c*r
       a21=d*j+m*e+f*p
       a22=d*k+n*e+f*q
       a23=d*l+e*o+f*r
       a31=g*j+h*m+i*p
       a32=g*k+h*n+q*i
       a33=g*l+h*o+i*r
       print(a11,a12,a13,"\n\n",a21,a22,a23,"\n\n",a31,a32,a33)