# input처리를 위해 try, catch 사용
# 1,11,111,...늘려가며 n으로 나누어 떨어지는지 확인

import sys

input = sys.stdin.readline

while True:
    try:
        n = int(input().strip())
         
    except:    
        break
    num=1
    count = 1
    while True:
            if num %n==0:
                break
            else:
                num = num*10+1
                count +=1
                
    print(count)   
            

