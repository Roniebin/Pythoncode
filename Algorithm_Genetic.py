
from math import sqrt
import random

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
        
# Genetic Algorithm start --------------------------------------------------------

# 초기 후보해 집합 G_o 생성
G_original=[['A','E','G','D','H','C','F','B'],
            ['B','F','C','H','D','G','E','A'],
            ['C','H','E','A','G','D','F','B'],
            ['D','F','B','C','H','G','E','A'],
            ['E','G','D','H','F','C','B','A'],
            ['F','C','H','D','G','E','A','B'],
            ['G','H','C','F','D','B','A','E'],
            ['H','G','D','F','C','B','A','E']
            ]

# 초기 후보해 집합을 숫자로 표현 ex) A==0 ,B==1
G_new=[]
G_next=[]
Evaluation=[]

for i in range(len(G_original)):
    temp=[]
    for j in range(len(G_original[0])):
        if G_original[i][j]=='A': temp.append(0)
        if G_original[i][j]=='B': temp.append(1)
        if G_original[i][j]=='C': temp.append(2)
        if G_original[i][j]=='D': temp.append(3)
        if G_original[i][j]=='E': temp.append(4)
        if G_original[i][j]=='F': temp.append(5)
        if G_original[i][j]=='G': temp.append(6)
    G_new.append(temp)
        

def Tournament_Selection(Evaluation):
    total_evaluation=sum(Evaluation)
    Evaluation_area=[]
    
    for i in range(len(Evaluation)):
        Evaluation_area.append(Evaluation[i]/total_evaluation)
  
    # 리스트를 내림차순으로 정렬하고, 인덱스와 값을 함께 가져온다.
    sorted_indices = sorted(enumerate(Evaluation_area), key=lambda x: x[1], reverse=True)

    # 정렬된 인덱스 중에서 상위 몇 개를 선택할지 정한다.
    top_indices = [index for index, value in sorted_indices[:4]]
    Evaluation_area.clear()
    
    for i in top_indices:
        temp1 =[]
        temp2=[]
        for j in range(len(G_new[i])):
            temp1.append(G_new[i][j])
            temp2.append(G_new[i][j])
        G_next.append(temp1)
        G_next.append(temp2)
       
        

def Cycle_Cross_function(crossover_rate) :
    mate =[]

    # 후보해 짝짓기 index 번호 기준 (1,2),(3,4),(5,6),(7,0)
    for i in range(1,7):
        mate.append(G_next[i])
    mate.append(G_next[6])
    mate.append(G_next[0])
        
    # 사이클 교차연산 시작
    for i in range(0,len(mate)-1,2):
        city=2      # 임의의 도시선택 => 2번 인덱스로 결정
        finded_city=0  # 처음부터 돌면서 중복이 되는게 있는지 확인하는 변수
        while mate[i][city]==mate[i+1][city] and city<len(mate)-2 and finded_city<len(mate)-2 : # 만약 시작지점이 같으면 시작지점을 다르게 해줄 while문,출발점과 마지막점은 지킴
            city+=1
            
        temp=mate[i][city]
        mate[i][city]=mate[i+1][city]
        mate[i+1][city]=temp
        finded_city=0
        while city<len(mate)-1 and finded_city<len(mate)-1 :
            if city!=finded_city: # 같은위치에서 찾으면 안됨
                if mate[i][city] == mate[i][finded_city]: # 만약 경로에 중복된 값이 존재하면
                    temp= mate[i][finded_city]            # 같이 교차연산 했던 경로와 스위칭하여 중복을 없앰
                    mate[i][finded_city]=mate[i+1][finded_city]
                    mate[i+1][finded_city]=temp
                    city=finded_city
                    finded_city=0                         # 중복체크변수는 중복해결 후 다시 처음으로돌아감(다음 중복체크를 대비)
                else :                                    # 같은위치가아니지만 중복되지않아서 다음값 탐색
                    finded_city+=1                        
            else :                                        # 같은 위치이면 중복해결변수가 그냥 넘어감
                finded_city+=1
    G_new.clear()
    for i in range(0,len(mate)):                          # 교차연산이 된 값들은 새로운새대 변수로 들어감
        G_new.append(mate[i])           
        
def Mutation_function(mutation_rate):
    if random.random() < mutation_rate:
        for i in range(len(G_new)):
            random_number = random.randint(0, 5)
            temp=G_new[i][random_number]
            G_new[i][random_number]=G_new[i][random_number+1]
            G_new[i][random_number+1]=temp


# G_o의 각 후보해를 평가
for i in range(0,len(G_new)):                          # 8가지 후부해를 전부 돈다
    value=0
    for j in range(0,len(G_new[0])-1):                   # 한 여행경로를 다 돌아본다
        value+=find_weight(nodes[G_new[i][j]],nodes[G_new[i][j+1]])
    value+=find_weight(nodes[G_new[i][-1]],nodes[G_new[i][0]])  # 가중치 평가할때는 돌아가는경로까지 포함
    Evaluation.append(value)
    

count=1000 # 반복수
crossover_rate=1 # 교차율
mutation_rate=0.01 # 돌연변이율
min_=100000000 # 처음 가중치
min_idx=[] # 가중치가 가장작은 경로를 받을 리스트

# repeat 
for i in range(count):
    Tournament_Selection(Evaluation)                         # 뉴세대
    Cycle_Cross_function(crossover_rate)                     # 사이클 교차 연산 수행
    Mutation_function(mutation_rate)                         # 돌연변이 연산
    
    Evaluation.clear()
    # G_new 의 각 후보해를 평가
    for j in range(0,len(G_new)):                            # 8가지 후부해를 전부 돈다
        value=0
        for k in range(0,len(G_new[0])-1):                   # 한 여행경로를 다 돌아본다
            value+=find_weight(nodes[G_new[j][k]],nodes[G_new[j][k+1]])
        value+=find_weight(nodes[G_new[j][-1]],nodes[G_new[j][0]])  # 가중치 평가할때는 돌아가는경로까지 포함
        Evaluation.append(value)
    
    t=Evaluation[0]                                          # 현재 세대 가장작은 가중치값
    for s in range(len(Evaluation)):
        if Evaluation[s]<t:
            t=Evaluation[s]
        
    new_evaluation=t
    new_evaluation_idx=Evaluation.index(new_evaluation)
    if min_>new_evaluation:                                  # 현재세대 최소값이 글로벌 최소보다 작으면
        min_=new_evaluation
        min_idx.clear()
        for k in G_new[new_evaluation_idx]:
            min_idx.append(k)

# 결과 값 출력
T=['A','B','C','D','E','F','G','H']

print("최단경로 이동경로 => ",end=' ')
for i in min_idx:
    print(T[i],end=' ')
    if i == min_idx[-1]:
        print(T[min_idx[0]])

print("최단여행경로 가중치 => ", min_)
