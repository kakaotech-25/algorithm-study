# 시간초과
# 저장할 배열 dp = [0]*(n+1)로 변경하여 해결
import sys
input = sys.stdin.readline
n = int(input())

def tile(n):
    dp = [0]*(n+1) # 저장할 배열
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    return dp[n-1]

print(tile(n))