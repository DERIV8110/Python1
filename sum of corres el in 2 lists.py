lst1=eval(input("enter elements of list 1: "))
lst2=eval(input("enter elements of list 2: "))
lst3=[]
if len(lst1)==len(lst2):
    for i in range(len(lst1)):
        lst3.append(lst1[i]+lst2[i])
    print("the third list with sums of corres el is: ",lst3)
else:
    print("please enter same number of elements in both lists")
