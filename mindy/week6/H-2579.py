'''
10
20
15
25
10
20
'''
import sys

input = sys.stdin.readline

n = int(input())

f=[0]*301
dp = [0] * (n+1)

for i in range(n):
    dp[i] = int(input())
    
f[0]  = dp[0]
f[1]  = dp[0]+dp[1]

    
for i in range(2,n):
    f[i] = max(dp[i-3]+f[i-1]+ f[i],dp[i-2]+ f[i]) 

print(max(f))