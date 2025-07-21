prod={}
i=0
while i in range(i+1):
    response=str(input('do you want to enter item/s(y/n)? '))
    if response=="y":
        item=str(input('enter item name: '))
        price=int(input('enter price: '))
        prod[item]=price    
    else:
        print(prod)
        k=0
        while k in range(k+1):
          response=str(input('do you want to search item/s(y/n)? '))
          if response=="y":
              seek=str(input('enter item you want find: '))
              print("price of",seek,"is:",prod[seek])
          else:
              break
        break

