import math
#for the form (x+a)**n
n=int(input('enter index(n)> '))
r=int(input('enter term preceeding the term you want to find(r-1)> '))
#if you want 4th term enter r-1=4-1=3
x=int(input('enter first term(X)> '))
a=int(input('enter second term(a)> '))
term=math.comb(n,r)*(x**(n-r))*(a**r)
print("the", r, "term is>", term)