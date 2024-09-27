# 런타임 에러
# dp = [0]*101로 변경하여 해결,,
import sys
input = sys.stdin.readline
t = int(input())

def tri(n):
    dp = [0]*101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n):
        dp[i] = dp[i-2] + dp[i-3] # 규칙

    return dp[n-1]

for _ in range(t):
    n = int(input())
    print(tri(n))