lst=eval(input("enter your list here: "))
              
length=len(lst)
lst2=[]
i=0

for i in range(i,length):
    lst2.append(lst[length-i-1])
    i+=1

print("your list:",lst,"\nreversed list",lst2)