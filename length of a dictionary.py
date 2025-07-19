fruit={}
l1=['Apple','banana','apple']
for index in l1:
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
print(len(fruit))
print(fruit)