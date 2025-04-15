str1=input("enter a string")
print("the",str1,"in reverse order is:")
length=len(str1)

for a in range(-1,(-length-1),-1):
    print(str1[a])

#we are simply using -ve index to print
#given string in reverse