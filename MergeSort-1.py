# 합병정렬
from math import floor

def Merge(arr,p,mid,q) :
    i=p # 첫번째 인덱스
    j=mid+1 # 또 다른 버킷의 인덱스
    k=p # 정렬될 배열의 인덱스
    
    while i<=mid and j<=q :
        if arr[i]>arr[j]:
            sorted_arr[k]=arr[j]
            j+=1
        else :
            sorted_arr[k]=arr[i]
            i+=1
            
        k+=1
        
    if i>mid:
        for idx in range(j,q+1):
            sorted_arr[k]=arr[idx]
            k+=1
    else:
        for idx in range(i,mid+1):
            sorted_arr[k]=arr[idx]
            k+=1
    
    for idx in range(p,q+1):
        arr[idx]=sorted_arr[idx]
    

def MergeSort(arr,p,q) : # 1칸이 될 때 까지 분할
    
    if p <q:
        mid= floor((p+q)/2)
        MergeSort(arr,p,mid)
        MergeSort(arr,mid+1,q)
        Merge(arr,p,mid,q)
        
        
    

arr=[8,6,8,0,5,4,36,8,6,886,6,43234]
number=10

sorted_arr=[0]*10

MergeSort(arr,0,number-1)
print(*arr)
