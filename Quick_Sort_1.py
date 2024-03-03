from math import floor

def QuickSort(bucket,left,right) :
    
    if left>=right:
        return 
    
    
    pivot=floor((left+right)//2)
    
    start=left+1
    end=right
    
    # 피봇값과 맨앞값을 바꿈
    temp=bucket[left]
    bucket[left]=bucket[pivot]
    bucket[pivot]=temp
    
    while start <= end :
        while start<=end and bucket[start]<= bucket[left] :
            start +=1
        while start <= end and bucket[end]>=bucket[left] and end>left:
            end-=1 
            
        if start <=end :
            temp =bucket[start]
            bucket[start]=bucket[end]
            bucket[end]=temp
        else :
            break
    
    temp=bucket[left]
    bucket[left]=bucket[end]
    bucket[end]=temp
    
    QuickSort(bucket,left,end-1)
    QuickSort(bucket,end+1,right)
    
bucket=[9,8,7,6,5,4,33,1,2]
number=9

    
QuickSort(bucket,0,number-1)

print(*bucket)

