# 못풀겠어서.. 참고 했습니다. 공부하고 더 풀어볼게요..ㅜㅜ
import sys
input = sys.stdin.readline

n = int(input())
re=0

arr=[]
for i in range(n):
    li= list(map(int,input().split()))
    arr.append(li)
    


def back(cnt, arr):
    global n, re
    if(cnt==n):
        broke_egg = 0
        for ar in arr:
            if ar[0] <=0: 
                broke_egg +=1
        re = max(re, broke_egg)
        return
    
    if arr[cnt][0] <=0:
        back(cnt+1, arr)
        return
    
    broke_egg =0
    for i in range(n):
        if i==cnt: continue
        if arr[i][0] <=0:
            broke_egg +=1
            continue
        
        arr[i][0] -=arr[cnt][1]
        arr[cnt][0] -=arr[i][1]
        back(cnt+1, arr)
        arr[i][0]+=arr[cnt][1]
        arr[cnt][0] += arr[i][1]
        
    if broke_egg == n-1:
        back(cnt+1, arr)
        
back(0,arr)
print(re)
    
    
