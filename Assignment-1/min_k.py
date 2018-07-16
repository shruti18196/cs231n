import numpy as np
k=3
s=np.array([5,4,3,2,1,10])
p=s.argsort()[:k]
print(p)
