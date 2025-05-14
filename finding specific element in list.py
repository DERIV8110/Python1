lst=eval(input("enter your list at once: "))
val=int(input("enter the element to search: "))
if val in lst:
     print("element is at index: ", lst.index(val))
else:
     print("element is not in the list")