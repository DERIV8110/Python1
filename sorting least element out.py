list=list()
sel=input("do you want to enter more elements? (true/false) ")
conv=bool(sel)
n=0

while n in range(n+1):          #infinite range where stop is 1 step ahead of n always
        
    if sel == "true":           #sel initiates and brings code into the loop, 
                                #where selection takes over of true of false
    
        user_input=list.append(input("enter the element:" ))
        n+=1
        selection=input("do you want to enter more elements? (true/false) ")
    elif selection == "false":
        print(list)