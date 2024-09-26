import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 301
ls = [0] * 301
for i in range(1,n+1):
    ls[i] = int(input())

dp[1] = ls[1]
dp[2] = ls[1] + ls[2]
dp[3] = max(ls[1]+ls[3], ls[2]+ls[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + ls[i], dp[i - 3] + ls[i - 1] + ls[i])

print(dp[n])