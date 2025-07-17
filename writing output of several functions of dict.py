dict={'a':27,'b':43,'c':25,'d':30
}
valA=''
for i in dict:
    if i>valA:
        valA=i
        valB=dict[i]
print(30 in dict)    #line3
print(valA)          #line1
print(valB)          #line2

mylst=list(dict.items())
mylst.sort()         #line5
print(mylst[-1])     #line4