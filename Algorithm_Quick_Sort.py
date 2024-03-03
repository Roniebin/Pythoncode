import sys
sys.setrecursionlimit(10**7)
import math
import pandas as pd
import datetime
import time  # time 모듈 추가


def QuickSort(data,left,right):
    if left>=right:
        return 
 
    #중간인덱스 찾기
    mid=math.floor((left+right)//2)
    #pivot변수 초기화
    pivot=0
    
    #가장왼쪽, 중간,가장 오른쪽중 중간값을 피봇으로 정할 if문
    # 가장왼쪽이 중간보다 클때,
    if(data[left]>data[mid]):
        #가장 오른쪽 값이 왼쪽보다 크면 왼쪽이 중간값이됨
        if(data[left]<data[right]):
            pivot=left
        #왼쪽이 가장크면 중간의 값이랑 가장오른쪽값이랑 비교
        else :
            if(data[mid]>data[right]):
                pivot=mid
            else :
                pivot=right
    else :
        if data[mid]<data[right]:
            pivot=mid
        else :
            if(data[left]>data[right]):
                pivot=left
            else :
                pivot=right
                
    #탐색전 피봇을 가장 처음값과 교환
    temp=data[left]
    data[left]=data[pivot]
    data[pivot]=temp
    
    #탐색할때 사용할 인덱스 
    i=left + 1  #피봇 다음인덱스부터 탐색시작
    j=right     #배열의 마지막인덱스부터 시작

    #탐색시작
    while i <= j:    # j가 i의 오른쪽에있을때(더이상 바꿀게 없다)
        while i<=j and data[left] >= data[i]:  # i가 배열 사이즈를 벗어나거나 , 피봇보다 큰걸 찾으면 stop
            i+=1
     
        while i<=j and data[left] <= data[j] and j > left: # j 가 배열사이즈를 벗어나거나, 피봇보다 작은걸 찾으면 stop
            j-=1
  
        if(i<=j):
            temp = data[i]
            data[i]=data[j]
            data[j]=temp
        else :
            break
        
    #엇갈림 => 더이상 탐색불가
    #피봇 위치를 정해줘야함 -> 피봇보다 작은 오른쪽숫자-> 마지막에 피봇왼쪽에 온 수 
    temp = data[left]
    data[left]=data[j]
    data[j] =temp
    
    QuickSort(data,left,j-1)
    QuickSort(data,j+1,right)


# 엑셀 파일 받아오기
file_name='input_quick_sort.xlsx'
df=pd.read_excel(file_name,sheet_name=0,engine='openpyxl',header = None,names='A')

number=df.index.stop
data=[0]*number

for i in df.index:
    data[i]=df['A'][i]

start_time = datetime.datetime.now()

QuickSort(data, 0, number-1)
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds() * 1000  # 밀리초 단위로 변환


f1=open('QuickSort_result.txt','w')
for i in range (number-1):
    f1.write(str(data[i])+'\n')
    print(data[i],end=' ')
   
    


f1.write("\n"+f"{elapsed_time:.6f} ms")
f1.close()


    