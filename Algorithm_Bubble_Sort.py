A=[5,32,7,2,4,7,8,9,1,53]
n=len(A)

for i in range(1,n):  # 1패스 부터 n-1까지 패스는 총 n-1번 함
    for j in range (1,(n-i)+1): # 이전값을 뽑아와야하기에 1부터 시작하고 1패스할때마다 j범위는 1씩 줄어듬
        if A[j-1]>A[j]:         # 앞의 위치가 현재위치보다 크면 자리체인지
            temp=A[j-1]
            A[j-1]=A[j]
            A[j]=temp
            
            
print(A)
    