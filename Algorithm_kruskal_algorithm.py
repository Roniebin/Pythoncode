class edgy :
    # 노트 시작지점부터 끝지점, 그리고 가중치 설정
    def __init__(self,start,end,distance):
        self.start=start
        self.end=end
        self.distance=distance

    
# -----------------------------------------------------------------
# 함수 정의

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
    
    
# -----------------------------------------------------------------
# main start 

V,E=map(int,input().split(" "))

Tree=[0]*V

edgys=[0]*E

node_num=V
parent=[0]*(node_num+1)

for i in range(E):
   a,b,c= map(int,input().split(" "))
   edgys[i]=edgy(a,b,c)

sorted_edgys=sorted(edgys,key=lambda x:x.distance)

# 노드들의 부모노드들은 자기자신으로 초기화
for i in range (1,node_num):
    parent[i]=i
    
d=0

for _edgy in sorted_edgys:
    # 두 노드의 루트 노드가 서로다르면 사이클 발생 하지 않은것
    if find_parent(parent,_edgy.start)!=find_parent(parent,_edgy.end):
       union_parent(parent,_edgy.start,_edgy.end)    

       d+=_edgy.distance
       
print(d)
       

    