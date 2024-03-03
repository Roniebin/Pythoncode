import numpy as np


n=20

d=[1,5,10,16]
INF=1000000
C=[INF]*(n+1)

C[0]=0

for j in range(1,n+1):
    for i in range(1,len(d)+1):
        if d[i-1]<=j and C[j-d[i-1]]+1<C[j]:
            C[j]=C[j-d[i-1]]+1
            
            
print(np.array(C))
         