
a,b=map(int,input().split(" "))

C=b    # 배낭의 용량
n=a   # 물건의 개수
w=[]     # 각 물건의 무게
v=[] # 각 물건의 가치

K=[[0]*(C+1) for _ in range(n+1)] 

for i in range(n):
    c,d=map(int,input().split(" "))
    w.append(c)
    v.append(d)


for i in range (0,n): # 배낭의 용량이 0일때 (어떤 물건도 못넣음)
    K[i][0]=0
    
for j in  range(0,C+1):   # 물건 0 이란 어떤 물건도 고려하지않을때 (배낭에 아무것도 안넣음)
    K[0][j]=0
    


for i in range(1,n+1):
    for j in range (1, C+1):    # j 는 각 배낭의 용량
        if w[i-1]>j:      # 물건 i 의 무게가 임시 배낭 용량을 초과하면
            K[i][j]=K[i-1][j]
        else :  # 물건 i를 배낭에 담지 않을 경우와 담을 경우를 고려
            K[i][j]=max(K[i-1][j], K[i-1][j-w[i-1]]+v[i-1])
            

print(K[n][C])
            
            
        
            
            
    

