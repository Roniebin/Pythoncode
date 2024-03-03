from math import sqrt

class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
        self.w=[]

nodes=[]                        # 각 좌표를 입력받을 배열
nodes.append(Node(0,3))         # A
nodes.append(Node(7,5))         # B
nodes.append(Node(6,0))         # C
nodes.append(Node(4,3))         # D
nodes.append(Node(1,0))         # E
nodes.append(Node(5,3))         # F
nodes.append(Node(2,2))         # G
nodes.append(Node(4,1))         # H

INF=100000000

def find_weight(first_node,second_node):        # 점과 점사이의 거리
    d=sqrt(pow((first_node.x-second_node.x),2)+pow((first_node.y-second_node.y),2))    
    return d
          
for i in range(len(nodes)):                     # 모든 경우의 가중치 입력 
    for j in range(len(nodes)):
        if i ==j :                              # 자기 자신한테로 가면 가중치가 0
            nodes[i].w.append(0)
        else :
            nodes[i].w.append(find_weight(nodes[i], nodes[j]))          
    
F=[]                                             # F는 가중치 그래프
for i in range(len(nodes)):                      # 가중치 그래프 생성
    for j in range(len(nodes)):
        F.append([i,j,nodes[i].w[j]])
    

# MST 구하기 (크루스칼)-----------------------------------------------------------------

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else :
        parent[a]=b

Tree=[0]*8

node_num=len(nodes)
parent=[0]*(node_num+1)

sorted_edgys=sorted(F,key=lambda x:x[2])

# 노드들의 부모노드들은 자기자신으로 초기화
for i in range (1,node_num):
    parent[i]=i
    
d=0
MST=[]
for _edgy in sorted_edgys:                          
    # 두 노드의 루트 노드가 서로다르면 사이클 발생 하지 않은것
    if find_parent(parent,_edgy[0])!=find_parent(parent,_edgy[1]):
       union_parent(parent,_edgy[0],_edgy[1])    
       MST.append([_edgy[0],_edgy[1],_edgy[2]])                  # MST그래프 생성
       d+=_edgy[2]

# ---------------------------------------------------------------
Front=[]                    # 0 -> 1 앞으로 가는배열
Back=[]                     # 1 -> 0 뒤로 가는 배열

for i in range(len(MST)):                           
    Front.append([MST[i][0],MST[i][1]])
    
for i in range(len(MST)):
    Back.append([MST[i][1],MST[i][0]])

result=[0,0,0,0,0,0,0,0]

# 제거된 경로 (다시 안돌려고)
result[Front[2][0]]+=1
result[Front[2][1]]+=1
Front_remove=[0,0,-1,0,0,0,0]  # A에서 시작점 
Back_remove=[0,0,0,0,0,0,0]

previous=0 # A 노드 시작
TSP=[0]

previous=Front[2][1]    # A노드 다음노드
TSP.append(previous)
  
count=0
while count<13:
    min=INF                            
    front_back_checking=0                       # 0이면 Front 1이면 Back 에서 가져옴
    
    removing_idx=0                              # 제거할 인덱스 번호 -> front_back_checking의 값에따라 Front 배열 또는 Back 배열에서 이값으로 제거함
    for i in range(len(Front)):
        if Front_remove[i]!=-1 :                # 제거된 간선이 아니면 실행
            if Front[i][0]==previous:           # 이전 값 과 같으면 예) 이전이 (0,6) 이면 다음엔 6으로 시작하는값을 찾아야함
                next=Front[i][1]                # 다음에 갈 값
                if min>result[next]:            # result 안의 값보다 작으면 => result안에는 이전에 몇번 방문했는지 저장
                    min=result[next]
                    min_idx=next
                    removing_idx=i
                    front_back_checking=0
                    
        if Back_remove[i]!=-1 :      
            if Back[i][0]==previous:
                next=Back[i][1]
                if min>result[next]:
                    min=result[next]
                    min_idx=next
                    removing_idx=i
                    front_back_checking=1
                    
    result[min_idx]+=1                            # 다음 방문할 인덱스에 방문 -> +1 해줌
    if front_back_checking==0 :                   # 프론트에서 다음 값을 가져옴
        Front_remove[removing_idx]=-1             # 그 간선 제거
        previous=Front[removing_idx][1]           # 간선의 끝점을 이전값에 저장
        TSP.append(previous)                      # TSP에 저장
       
    else :
        Back_remove[removing_idx]=-1
        previous=Back[removing_idx][1]
        TSP.append(previous)
    count+=1                                       

for i in range(1,len(TSP)):                        # TSP의 중복제거
    sub_string=TSP[:i]
    if TSP[i] in sub_string : 
        if i !=len(TSP)-1:
            TSP[i]=-1

# 결과 ---------------------------------------------------------------
M=['A','B','C','D','E','F','G','H']
new_TSP_order=[]
new_TSP=[]
for i in range (len(TSP)):
    if TSP[i]!=-1:
        new_TSP_order.append(M[TSP[i]])
        new_TSP.append(TSP[i])
print("근사해 이동순서 " ,*new_TSP_order)

approximation_weight=0
for i in range(0,len(new_TSP)-1):
   approximation_weight+=find_weight(nodes[new_TSP[i]],nodes[new_TSP[i+1]])
print("근사해 이동거리 ", approximation_weight)


optimal_TSP=[0,7,5,2,4,3,1,6,0]
optimal_weight=0
for i in range(0,len(optimal_TSP)-1):
   optimal_weight+=find_weight(nodes[optimal_TSP[i]],nodes[optimal_TSP[i+1]])
print("최적해 이동거리 ", optimal_weight)

