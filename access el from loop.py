x=(1,4,9,16,25,36,49,64,81,100)
x1=49
i=0
while i<len(x):
    if(x[i]==x1):
        print("found at idx", i)
        break
    else:
        print("finding...")
        i+=1
print("end of loop")