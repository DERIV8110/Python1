lst=[]
selection=input("do you want to enter more elements? (t/f) ")
                            #selection initiates code and brings code into the loop                                                                
n=0

while n in range(n+1):      #infinite range where stop is 1 step ahead of n always    
    if selection=="t":
        element=input("enter the element:" )
        lst.append(element)
        selection=input("do you want to enter more elements? (t/f) ")
        
                            #where selection takes over of true of false
    elif selection == "f":
        frequency=input("enter element whose frequency you want to know: ")
        cnt=lst.count(frequency)
        print("\n\nyour list is: ",lst,"\nfrequency of",frequency,"is",cnt)
        break

    