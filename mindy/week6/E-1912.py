# 하나씩 더해가며 최대일 경우 비교
import sys
input = sys.stdin.readline

n = int(input())

f = list(map(int, input().split()))


for i in range(1,n):
    f[i] = max(f[i],f[i]+f[i-1])
    
    
        
print(max(f))