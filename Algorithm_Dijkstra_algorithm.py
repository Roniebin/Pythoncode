import datetime


number =10
INF=100000000
citys=["서울", "천안", "원주", "논산", "대전", "강릉", "포항", "대구", "광주", "부산"]

# 전체그래프 초기화
# 서울, 천안, 원주, 논산, 대전,강릉,포항,대구,광주, 부산
A=[[0,12,15,INF,INF,INF,INF,INF,INF,INF],
[12,0,INF,4,10,INF,INF,INF,INF,INF],
[15,INF,0,INF,INF,21,INF,7,INF,INF],
[INF,4,INF,0,3,INF,INF,INF,13,INF],
[INF,10,INF,3,0,INF,INF,10,INF,INF],
[INF,INF,21,INF,INF,0,25,INF,INF,INF],
[INF,INF,INF,INF,INF,25,0,19,INF,5],
[INF,INF,7,INF,10,INF,19,0,INF,9],
[INF,INF,INF,13,INF,INF,INF,INF,0,15],
[INF,INF,INF,INF,INF,INF,5,9,15,0]]

V=[False]*10    # 방문한 노드인지
D=[0]*10    # 거리
result_D=[]

# 가장 최소 거리를 가지는 정점 반환
def get_Minimum_Index():
    min=INF 
    index=0 
    for i in range(0,number):
        if(D[i]<min and V[i] is False):
            min=D[i]
            index=i
             
    return index 



start_time = datetime.datetime.now()


# 다익스트라 수행
def dijkstra(start) :
    for i in range (0,number):
        D[i]=A[start][i]
        
    V[start]=True   # 시작점은 방문처리
    for i in range(0,number-1):
        current=get_Minimum_Index()
        V[current]=True 
        for j in range(0,number):
            if(V[j] is False):
                if D[current]+A[current][j] < D[j]:
                    D[j]= D[current]+A[current][j]
                    
                    
for i in range(len(citys)):
    print("    ",citys[i],end='')
print()

start_time = datetime.datetime.now()

for i in range(number):    
    V=[False]*10    # 방문한 노드인지
    D=[0]*10    # 거리
    dijkstra(i)
    result_D.append(D)
            
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds() * 1000  # 밀리초 단위로 변환
            
    
for i in range(len(result_D)):
    print(citys[i],end='  ')
    for j in range(len(result_D[i])):
        emp="     "
        if len(str(result_D[i][j]))==1:
            emp+=" "
        
        print(result_D[i][j],emp,end=' ')
    print()


print("실행시간 : {0:0.5f}".format(elapsed_time))
            
            
            
            
            
        
    
    
        

