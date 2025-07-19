box={}              #box={'biscuit':1,'cake':3}
jars={'jam':4}
crates={}           #crates={'box':('biscuit':1,'cake':3),'jars':('jam':4)}
box['biscuit']=1
box['cake']=3
crates['box']=box
crates['jars']=jars
print(len(crates['box']))