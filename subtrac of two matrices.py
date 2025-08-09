import numpy as np
a1=np.array(([1,2,3,4],
             [5,6,7,8]))  #it is compulsory to use double brackets,
                              #to pass comma separated argu at once.
a2=np.array(([1,3,4,4],
             [5,6,7,8]))
a3=np.subtract(a1,a2)
print(a3)