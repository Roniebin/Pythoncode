A=[6,4,3,5,7,8,9,1,2,88]
n=len(A)

for i in range(1,n):
    CurrentElement=A[i] # 정렬안된 부분의 가장 왼쪽원소
    j=i-1
    while(j>=0) and A[j]>CurrentElement:
        temp=A[j+1]
        A[j+1]=A[j]
        A[j]=temp 
        j=j-1
        
    A[j+1]=CurrentElement
print(A)