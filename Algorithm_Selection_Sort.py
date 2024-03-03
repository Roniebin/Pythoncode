A=[6,4,3,2,1,10,7,8]

n=len(A)

for i in range(0,n):    
    min=i                   # 스타트 위치를 최소로 일단둠
    for j in range(i+1,n):  # 스타트 다음위치부터 끝까지돌림
        if A[j]<A[min]:     # 스타트 다음위치부터 최소인덱스안과비교해 가장 최소값의 인덱스번호 추출
            min=j
    
    temp=A[i]
    A[i]=A[min]
    A[min]=temp
    
    
print(A)
     
    
    