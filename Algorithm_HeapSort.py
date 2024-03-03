from math import floor

f=open('input.txt','r')
f1=open('output.txt','w')

A=[-1] # 0 번째 인덱스는 없는거

while True:
    line = f.readline()
    if not line: # 파일 읽기가 종료된 경우
        break
    A.append(int(line))
    
n=len(A)-1 # 노드의 개수 (마지막인덱스)

def BuildHeap():
    for i in range (floor(n/2),0,-1): # i번을 루트노드로 최대힙을 이루도록 해주는 함수
        DownHeap(i)
   
def DownHeap(i):
    leftChild=2*i
    rightChild=(2*i)+1
    
    if leftChild <=heapSize and A[leftChild] > A[i]: # 노드 개수를 벗어나지않고, 왼쪽자식이 부모노드보다 크면
        bigger=leftChild    # 큰 값의 인덱스를 bigger에 저장 (초기화 과정)
    else :
        bigger=i 
        
    if rightChild <=heapSize and A[rightChild] > A[bigger]:
        bigger=rightChild   # 오른쪽자식이 더크면 bigger에 저장
    
    if bigger!=i : # 부모, 왼쪽, 오른쪽 노드 비교 후 제일 큰 값이 부모가아니면 (최대힙 성립 x)
        temp = A[i]
        A[i]=A[bigger]
        A[bigger]=temp 
        DownHeap(bigger) # 바뀌고 나서 그자리에서 부터 또 밑으로 최대힙 되도록 함수 호출
                
result=[]
heapSize=n 

# 힙생성
BuildHeap()

for i in range(1,n+1):
    temp=A[1]               # 루트와 힙의 마지막 노드교환
    A[1]=A[heapSize]
    A[heapSize]=temp

    heapSize=heapSize-1     # 힙의 크기 감소
    DownHeap(1)              # 위배된 힙 조건을 만족시킴


for i in range(1,len(A)):
    f1.write(str(A[i])+"\n")