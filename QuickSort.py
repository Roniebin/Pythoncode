def QuickSort(bucket,start,end):
    if start >=end:
        return 
    
    key=start #키는 첫번째 원소(피봇)
    i=start+1 #키 값의 바로 오른쪽 인덱스 /왼쪽 출발지점
    j=end
    temp=0
    
    while(i<=j): #엇갈릴때 까지 반복
        while(i <= j and bucket[i]<=bucket[key]):
            i+=1
        
        while(i <= j and bucket[j]>=bucket[key] and j>start):
            j-=1
            
        if i>j: # 현재 엇갈린 상태면 키값과 교체
            temp=bucket[j]
            bucket[j]=bucket[key]
            bucket[key]=temp
        else:
            bucket[j]=bucket[i]
            temp=bucket[j]
            
            bucket[i]=temp
            
    QuickSort(bucket,start,j-1)
    QuickSort(bucket,j+1,end)
    

number=10
array =[1,10,5,8,7,6,4,3,2,9]

QuickSort(array,0,number-1)

print(*array)