import numpy as np

s=input()
t=input()
S=s
T=t
m=len(S)
n=len(T)
a=0 

E=[[0]*(n+1) for _ in range(0,m+1)]

# 행 초기화
for i in range(0,m+1):
    E[i][0]=i
    
# 열 초기화    
for j in range(0,n+1):
    E[0][j]=j 
    
for i in range (1,m+1):
    for j in range(1,n+1):
        
        if S[i-1]==T[j-1] : # 문자열들은 0부터 시작하기때문에 i-1
            a=0
            print("c ",T[i])
        else:
            a=1
        E[i][j]=min(E[i][j-1]+1, E[i-1][j]+1 , E[i-1][j-1]+a)
        if E[i][j]==E[i][j-1]+1 :
            print("a ",T[i])
        elif E[i][j]==E[i-1][j]+1 :
            print("d ",T[i])
        elif E[i][j]==E[i-1][j-1]+a:
            print("m ",T[i])
            
    
    
print(np.array(E))
        