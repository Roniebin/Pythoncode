a=int(input())

start =1
count=0

min=99999999
while start<a:
    if (a%start==0): # 나눠지면
        count=(a//start)-1  # 1열부터 몇칸인지
       
        count+=start-1  # 1뺴고 더해줌
       
        if min>count:
            min=count
        
    start+=1
    
        
print(min)