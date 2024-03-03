from math import floor

def Merge(bucket,p,middle,q):
    i=p                                      #첫번째 버킷의 인덱스
    j=middle+1                               #또다른 버킷의 인덱스
    k=p                                      #정렬될 배열의 인덱스
    
    while(i<=middle and j<=q):              #첫번째 버킷이나 두번째 버킷이 끝날때 까지
        if bucket[i]<=bucket[j]:
            sorted_bucket[k]=bucket[i]
            i+=1
        else :
            sorted_bucket[k]=bucket[j]
            j+=1
    
        k+=1
    
    if(i>middle):
        for idx in range(j,q+1):
            sorted_bucket[k]=bucket[idx]
            k+=1
    else:
        for idx in range(i,middle+1):
            sorted_bucket[k]=bucket[idx]
            k+=1
    
    for idx in range(p,q+1):           
        bucket[idx]=sorted_bucket[idx]


def MergeSort(bucket,p,q):  # 크기 1개까지 나누기
    if p<q:
        middle= floor((p+q)/2)
        MergeSort(bucket,p,middle)
        MergeSort(bucket,middle+1,q)
        Merge(bucket,p,middle,q)
    

array=[37,10,22,30,35,13,25,24]
number=8
sorted_bucket=[0]*8

MergeSort(array,0,number-1)

print(*array)