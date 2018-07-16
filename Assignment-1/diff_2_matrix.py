import numpy as np
a=np.array([1,6,2,5])
b=np.array([5,6,7,8])
print(pow((a[0]-b[:]),2))
dis=np.zeros((4,4))
for i in range(4):
    dis[i,:]=pow(np.sum(pow((a[i]-b[i,:]),2)),0.5)
print(dis[:])

for i in range(4):
    for j in range(4):
        dis[i,j]=pow(np.sum(pow((a[i]-b[j]),2)),0.5)
print(dis)
