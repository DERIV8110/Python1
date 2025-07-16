#build some dictionary
dict={"a":1,"b":2,"c":3,"d":4}
v=int(input("enter value to get corres. key: "))
for key,value in dict.items():
    if value==v:
        print(key)