A=[30,60,90,10,40,80,40,20,10,60,50,30,40,90,80]
n=len(A)

print(A)
for h in range(5,0,-1): # h == each_gap
    print("h가 ",h)
    
    for i in range(h, n):
        CurrentElement=A[i]
        j=i 
        
        while j>=h and A[j-h]>CurrentElement:
            A[j]=A[j-h]
            j=j-h
        
        A[j]=CurrentElement
    
    print(A)
print(A)

        
