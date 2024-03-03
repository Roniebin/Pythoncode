import math
import pandas as pd
import numpy as np
import time

# CSV 파일 경로
csv_file_path = 'input.csv'  
M = pd.read_csv(csv_file_path).to_numpy()    

S_idx=[]            # Max_idx를 통해 얻을 최고의 det을 만들 idx들
Max_V=0
Max_idx=0

start_time = time.time()

for i in range(20): # 모든 S를 채우기 위함  
    Max_idx=0
    for j in range(10000):
        if j not in S_idx :                             #j는 이미 선택된 열을 가져오면 안됨
            temp=M[:,S_idx+[j]]
            V=np.linalg.det(np.dot(temp.T, temp))
         
            if Max_V<V:
                Max_V=V
                Max_idx=j
    S_idx.append(Max_idx)

A=M[:,S_idx]
Max_V=math.sqrt(abs(np.linalg.det(np.dot(A.T, A))))

end_time = time.time()

print("최대값 => ", Max_V)
print("실행시간 => ",end_time - start_time)
print("가져온 열= > ",S_idx)
print("performance matrix value => ",Max_V//((end_time - start_time)/1000000))