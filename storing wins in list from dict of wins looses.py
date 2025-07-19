name_score={}
name_win_percent={}
i=0
lst=[]
while i in range(i+1):
    response=str(input('do you want to enter team name(y/n)? '))
    if response=="y":
        name=str(input('enter team name: '))
        score=eval(input('enter [win,loose]: '))
        lst.append(score[0])
        name_score[name]=score       
        i+=1
    else:
        break

print(name_score)
print(lst)