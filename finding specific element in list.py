lst=[]
selection=input("do you want to enter more elements? (true/false) ")
                            #selection initiates code and brings code into the loop                                                                
n=0

while n in range(n+1):      #infinite range where stop is 1 step ahead of n always    
    if selection=="true":
        element=input("enter the element:" )
        lst.append(element)
        selection=input("do you want to enter more elements? (true/false) ")
        
                            #where selection takes over of true of false
    elif selection == "false":
        idx=float(input("enter the element to search: "))
        print("element is at index: ",lst[int(idx)] )
        break