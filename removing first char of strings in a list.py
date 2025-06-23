lst1=eval(input("enter your list: "))
lst2=[]
#lst1=[apple,banana]
#lst2=[pple,anana]
#i should better kill myself than thinking how cumbersome solution is.
for i in range(len(lst1)):
    lst2.append(lst1[i][1:]) #fuck this line 

print("List after removing first characters:")
print(lst2)