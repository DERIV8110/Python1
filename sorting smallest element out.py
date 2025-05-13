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
        sorted_list=sorted(lst)
        print("your list is: ",sorted_list,"\nsmallest element in list is: ",sorted_list[0])
        break

    