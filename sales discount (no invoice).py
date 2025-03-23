price=float(input('enter sales amount: '))
tax_rate=float(input('enter sales tax rate(5-12%): '))
disc1=0
amt_payable1=0
print("sales amount: ",price)
print("sales tax: ",tax_rate)
if price<20000:
    discrate1=10
    disc1=price-(price*discrate1/100)     #price has been discounted here
                                          #and added to discounted price
    amt_payable1=disc1+(disc1*tax_rate/100)     #tax has been added on the discounted rate
                                                #and added to amount payable
    print('amount payable: ',amt_payable1,"\n@10 percent discountrate")
else:
    discrate2=17.5
    disc1=price-(price*discrate2/100)    #price has been discounted here
                                         #and added to discounted price
    amt_payable2=disc1+(disc1*tax_rate/100)     #tax has been added on the discounted rate
                                                #and added to amount payable
    print('amount payable: ',amt_payable1, "\n@17.5 percent discountrate")

