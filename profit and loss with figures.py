n=5

total_cost_price=0
total_selling_price=0

for i in range(1,n+1):
    
    cost_price=int(input(f"enter cost price of the item {i}>"))
    total_cost_price+=cost_price
    
    selling_price=int(input(f"enter selling price of the item {i}>"))
    total_selling_price+=selling_price
    
    if cost_price>selling_price in i:
        print("loss of> ",cost_price-selling_price)
    if selling_price>cost_price in i:
        print("profit of> ",selling_price-cost_price)

if total_cost_price>total_selling_price:
    print("loss has occured")
if total_selling_price>total_cost_price:
    print("profit has occured")












