import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

left, right =0, n-1

re =abs(arr[left]+arr[right])
re_left =0
re_right=n-1

while left<right:
    tmp = arr[left]+arr[right]
    
    if abs(tmp) <= re:
        re_left = left
        re_right=right
        re = abs(tmp)
        
        if re == 0:
            break
    if tmp <0:
        left+=1
        
    else:
        right-=1
        
    
print(arr[re_left],arr[re_right])