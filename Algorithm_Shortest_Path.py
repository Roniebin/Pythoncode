import datetime

number=10   # 노드개수
INF=100000000

citys=["서울", "천안", "원주", "논산", "대전", "강릉", "포항", "대구", "광주", "부산"]

# 전체그래프 초기화
# 서울, 천안, 원주, 논산, 대전,강릉,포항,대구,광주, 부산
G=[[0,12,15,INF,INF,INF,INF,INF,INF,INF],
[12,0,INF,4,10,INF,INF,INF,INF,INF],
[15,INF,0,INF,INF,21,INF,7,INF,INF],
[INF,4,INF,0,3,INF,INF,INF,13,INF],
[INF,10,INF,3,0,INF,INF,10,INF,INF],
[INF,INF,21,INF,INF,0,25,INF,INF,INF],
[INF,INF,INF,INF,INF,25,0,19,INF,5],
[INF,INF,7,INF,10,INF,19,0,INF,9],
[INF,INF,INF,13,INF,INF,INF,INF,0,15],
[INF,INF,INF,INF,INF,INF,5,9,15,0]]

# 배열 D를 INF로 초기화
D=[INF]*number
result_D=[]
T=[]


# 다음 경로 찾아오기
def next_Path() :
    min=INF
    index=0 
    
    for i in range (number):
        if D[i]<min and i not in T:
            min=D[i]
            index=i 
    return index


# 다엑스트라 알고리즘 -------------------------------------------------------------
def Shortest_Path(D):
    
    count=0
    while count<number:         # 최단거리가 확정되지 않은 점이 있으면 (모든 점의 개수만큼 돌려야 모든 점의 최단거리를 구할수있음)
        v_min=next_Path()       # 다음 경로 가져오기
        T.append(v_min)         # 경로 방문
        
        for w in range (number):
            if w not in T:
                if D[w] > D[v_min]+G[v_min][w]: # 간선완화 : 우회해서 가는 가중치가 원래가중치 보다 작으면 업데이트
                    D[w]=D[v_min]+G[v_min][w]
                    
        count+=1
                    
        
# 실행시간 함수
start_time = datetime.datetime.now()

for i in range(number):
    D=G[i]                  # 시작점에 대한 가중치 초기화
    T.clear()
    T.append(i)             # 시작점은 미리 T 영역안으로 
    Shortest_Path(D)        # 다엑스트라 알고리즘 시작
    result_D.append(D)      # 결과 가중치 저장
  
  
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds() * 1000  # 밀리초 단위로 변환

    
# 출력               
print("도시간 최단 거리:")
print("\t" + "\t".join(citys))  # 도시 이름 출력

for i in range(len(citys)):
    print(citys[i] + "\t" + "\t".join(map(str, result_D[i])))

print()
print("실행시간 : {0:0.5f}".format(elapsed_time))
                
                


            
        
        
        
    

