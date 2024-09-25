'''
5
    7 -> 7
   3 8 -> 3
  8 1 0 -> 8 
 2 7 4 4 -> 7
4 5 2 6 5 -> 5
'''

import sys

input = sys.stdin.readline

n = int(input())

dp = [0]*n

for i in range(n):
    dp[i] = list(map(int, input().split()))
    
for i in range(1,n):
    for k in range(len(dp[i])):
        if k ==0:
            dp[i][k] = dp[i-1][k] + dp[i][k]
        elif k == len(dp[i])-1:
            dp[i][k] = dp[i-1][k-1] + dp[i][k]
        else:
            dp[i][k] = max(dp[i-1][k-1],dp[i-1][k])+dp[i][k]
print(max(dp[n-1]))