import sys


T=[]        # 방문한 노드 저장
F=[]        # 간선 저장
Front=[[0,1,3],[3,1,4],[0,3,2],[1,2,1],[1,5,2],[2,5,1],[3,5,7],[0,4,4],[3,4,5],[4,5,9]]

N=len(Front)
edgys=[0]*N     

D=[999]*6       # 무한을 999로 표현

for i in range(N):
    if i<10:
        edgys[i]=Front[i]

# 시작시 2번(C) 노드 방문 후 D[2] 초기화
T.append(2)
D[2]=0

for i in range (0,len(edgys)):
    if edgys[i][0]==2 and edgys[i][1] not in T:         # 만약 간선의 시작이 2이고 ,끝이 T 공간의 밖에있으면 
        D[edgys[i][1]]=edgys[i][2]
        
    elif edgys[i][1]==2 and edgys[i][0] not in T:        # 만약 간선의 끝이 2이고 ,끝이 T 공간의 밖에있으면 
        D[edgys[i][0]]=edgys[i][2]
        
        
while len(T) < 6:
    min=999
    min_idx=0
    
    for i in range (0,len(D)):
        if D[i] < min and i not in T:        # T안에 없는노드 (공간 밖) 중에서 가장 작은 가중치를 가지는 노드찾기
            min=D[i]
            min_idx=i
    
    T.append(min_idx)
    
    for i in range(0,len(edgys)):
        if edgys[i][0]==min_idx and edgys[i][1] not in T:
            if D[edgys[i][1]] >edgys[i][2]:         # 이번에 들어온게 원래있던 가중치보다 작으면 갱신
                D[edgys[i][1]]=edgys[i][2]
                
            
        elif edgys[i][1]==min_idx and edgys[i][0] not in T:
            if D[edgys[i][0]] > edgys[i][2]:         # 이번에 들어온게 원래있던 가중치보다 작으면 갱신
                D[edgys[i][0]]=edgys[i][2]
                
        # 다음 확장시킬 노드의 간선이고 T공간 밖으로의 방향으로, 그 노드와 연결된 가장 작은 가중치의 라인을 연결
        if edgys[i][1] == min_idx and edgys[i][2]==min:
            F.append(edgys[i])
        elif  edgys[i][0] == min_idx and edgys[i][2]==min:
            F.append([edgys[i][1],edgys[i][0],edgys[i][2]])
         
for i in range(len(F)):
    print("({},{},{})".format(F[i][0],F[i][1],F[i][2]))

