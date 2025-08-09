import numpy as np
adict={1:"a",2:"b",3:"c",4:"d"}
ar1=np.fromiter(adict,dtype=np.int32)
print(ar1)  #prints array
print(ar1.dtype)   #prints datatype of ar1