import datetime

number =10
INF=100000000
citys=["서울", "천안", "원주", "논산", "대전", "강릉", "포항", "대구", "광주", "부산"]

# 전체가중치 초기화
# 서울, 천안, 원주, 논산, 대전,강릉,포항,대구,광주, 부산
D=[[0,12,15,INF,INF,INF,INF,INF,INF,INF],
[12,0,INF,4,10,INF,INF,INF,INF,INF],
[15,INF,0,INF,INF,21,INF,7,INF,INF],
[INF,4,INF,0,3,INF,INF,INF,13,INF],
[INF,10,INF,3,0,INF,INF,10,INF,INF],
[INF,INF,21,INF,INF,0,25,INF,INF,INF],
[INF,INF,INF,INF,INF,25,0,19,INF,5],
[INF,INF,7,INF,10,INF,19,0,INF,9],
[INF,INF,INF,13,INF,INF,INF,INF,0,15],
[INF,INF,INF,INF,INF,INF,5,9,15,0]]

start_time = datetime.datetime.now()

# 플로이드 와샬

for k in range(0, number):
    for i in range(0, number):
        if i!=k:
            for j in range(0, number):
                if j!=k and j!=i:
                    D[i][j] =min(D[i][k]+D[k][j],D[i][j])

end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds() * 1000  # 밀리초 단위로 변환
                  
                  
#출력                            
for i in range(len(citys)):
    print("     ",citys[i],end='')
print()

for i in range(number):    
    print(citys[i],end=' ')
    for j in range(number):
        emp="    "
        if len(str(D[i][j]))==1:
            emp+=" "
        print(" ",D[i][j],emp,end=" ")
        
    print()

print()
print("실행시간 : {0:0.5f}".format(elapsed_time))
