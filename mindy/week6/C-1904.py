# 자꾸 런타임에러가 발생해서 찾아보니 n이 1일때 문제가 생긴다.
# 그래서 f=[0]*(n+1)에서 변경함
import sys
input = sys.stdin.readline

n = int(input())

f=[0]*1000001

f[1]=1
f[2]=2
for i in range(3,n+1):
    f[i] = (f[i-1]+f[i-2])%15746
    
print(f[n])
    