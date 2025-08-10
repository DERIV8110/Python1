import numpy as np
list1=[1,2,3,4,5]
ar1=np.fromiter(list1,dtype=np.int32,count=3)   #count prints specified first n elements
print(ar1)