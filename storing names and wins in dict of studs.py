n=int(input("enter number of students:"))
compwinner={}                 #empty dict
for a in range(n):
    key=input("enter name of student: ")
    value=int(input("enter number of wins: "))
    compwinner[key]=value     #appends dict with key value pairs together in each loop
print("the dictionary now is: ","\n",compwinner)