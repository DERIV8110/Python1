import json        #json outputs cleaner output in separate lines rather than 1 single line
sentence= "this is a super idea this idea will change the idea of learning"
words=sentence.split()
d={}
for one in words:
    key=one           #adds i one by one as keys into dict
    if key not in d:     #true cuz the key not in dict
        cnt=words.count(key)      #counts words and adds to value of i (key)
        d[key]=cnt
print("counting frequencies in list \n",words)
print(json.dumps(d,indent=2))