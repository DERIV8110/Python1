x1=float(input('enter number of items> '))
if x1<0:
    print("invalid input")
else:
    if x1<10:
        print(x1*120, "Total")
    if 10<x1<99:
        print(x1*100, "Total")
    if 100<x1:
        print(x1*70, "Total")

    
