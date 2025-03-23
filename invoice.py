import datetime
now=datetime.datetime.now()
dtm=str(now)
item="amul butter 100gms"
unit_price=float(input("enter unit price of the item: "))
qty=int(input("enter quantity of the item: "))
tax=int(input("enter tax rate: "))
value=unit_price*qty
amt_payable=value+value*tax/100
print("-"*65)
print("\t\t\t\tInvoice")
print("-"*65)
print("date:{0:55s}".format(dtm))
print("-"*65)
print("{0:<25s}".format(item),end="") #<25s means that string characters should be <25 
print("{0:>7.2f}".format(unit_price),end="")
print("{0:>10d}".format(qty),end="")
print("{0:>14.2f}".format(value))
print("Tax:{0:>57.2f}".format(tax))
print("-"*65)
print("amount payable:{0:>46.2f}".format(amt_payable))