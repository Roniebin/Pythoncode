d=[10,20,5,15,30]
n=4
INF=100000000
C=[[0]*(n+1) for _ in range(n+1)]
P=[[0]*(n+1) for _ in range(n+1)]

for L in range(1,n): # L은 부분문제의 크기를 조절하는 인덱스
    for i in range(1,(n-L)+1):  # i 는 C의 시작점이고, 부분문제가 커질수록 L로인해 작아짐 
        j=i+L
      
        C[i][j]=INF 
       
        for k in range(i,j): # k 는 안에서 어떻게 자를 것인가 결정   (A1 X A2) X A3  or A1 X (A2 X A3)
            temp=C[i][k]+C[k+1][j] + d[i-1]*d[k]*d[j]
            
            if temp < C[i][j]:
                C[i][j]=temp 
                P[i][j]=k
            

print(C)

# 가장 최적의 계산 순서
def best_order(P,i,j):
    if i==j:
        print("M",i,end=' ')
    else :
        k=P[i][j]
        print("(",end=' ')
        best_order(P,i,k)
        best_order(P,k+1,j)
        print(")",end=' ')
        
best_order(P,1,n)

