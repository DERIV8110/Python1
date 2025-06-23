lst1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lst2=[]

for i in range(len(lst1)):
        lst2.append(lst1[i]*(i+1))
print(lst2)