n=int(input('enter the term you want to find: '))
k=1.61           #k is golden ratio~1.61
F = (k**n - (1-k)**n) / 2.23     #binet's formula 

print("the",n,"th term of fibonacci sequence is:s",F)
print("round off error might occur due to floating point numbers")