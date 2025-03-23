i=1
tot_transx=0
tot_sales=0
while i<=7:
    transx=float(input(f"Transaction made on day {i}: "))
    sold=float(input(f"Items sold on day {i}: "))
    tot_transx+=transx
    tot_sales+=sold
    i+=1
print("Total sales made: ",tot_sales)
print("Total transactions made: ",tot_transx)
print("Average sales per transaction: ",tot_sales/tot_transx)