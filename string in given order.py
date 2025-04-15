str1=input("enter string: ")
print("the",str1,"in reverse order is:")
length=len(str1)
i=0
for a in range(-1,(-length-1),-1):
    print(str1[i],"\t",str1[a])
    i+=1
# we are simply using -ve index to print
# given string in reverse
# i is used as +ve index like if len=5 s[-1+5]=s[4]
# which is used as +ve index
# \t to give space between
# each letter