price=float(input('enter a number: '))
disc1=0
disc2=0
if price<20000:
    disc1+=price+price*0.10+price*0.12
    print('amount payable: ',disc1)
else:
    disc2+=price+price*0.175+price*0.12
    print('amount payable: ',disc2)
