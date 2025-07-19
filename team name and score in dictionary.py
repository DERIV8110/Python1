name_score={}
i=0
while i in range(i+1):
    response=str(input('do you want to enter team name(y/n)? '))
    if response=="y":
        name=str(input('enter team name: '))
        score=eval(input('enter [win,loose]: '))
        name_score[name]=score    
    else:
        break

print((name_score))