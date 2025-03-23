item_code=input("enter item code (A) Apparel or (F) Footwear> ")
sp=float(input("enter selling price (per unit) of item> "))
amt_payable=0

if item_code=="a":
    item_code="Apparel"
    if sp<=1000:
        sgst=cgst=3
        CGST=sp*cgst/100
        SGST=sp*sgst/100
        amt_payable=sp+sp*sgst/100+sp*cgst/100
    else:
        sgst=cgst=6
        CGST=sp*cgst/100
        SGST=sp*sgst/100
        amt_payable=sp+sp*sgst/100+sp*cgst/100

elif item_code=="f":
    item_code="Footwear"
    if sp<=500:
        sgst=cgst=5
        CGST=sp*cgst/100
        SGST=sp*sgst/100
        amt_payable=sp+sp*sgst/100+sp*cgst/100
    else:
        sgst=cgst=18
        CGST=sp*cgst/100
        SGST=sp*sgst/100
        amt_payable=sp+sp*sgst/100+sp*cgst/100
#now formatting invoice
print("-"*65)
print("\t\t\t\tINVOICE")
print("-"*65)
print("Item:{0:s}".format(item_code))
print("Price:{0:f}".format(sp))
print("\t\t\t\tCGST:{0:f}".format(CGST))
print("\t\t\t\tSGST:{0:f}".format(SGST))
print("-"*65)
print("Amount Payable:{0:f}".format(amt_payable))
print("-"*65)