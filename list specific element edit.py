lst1=list(eval(input("enter your list: ")))
for i in range(len(lst1)):
    if lst1[i]>10:
        lst1[i]=10

print("your list after removing numbers greater than 10 is: ",lst1)