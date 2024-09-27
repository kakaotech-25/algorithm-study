#unsolved
#백로그
import sys
input = sys.stdin.readline

n = int(input())
col = []
for i in range(n):
    col.append(list(map(int, input().split())))

def sum(n):
    dp = [[0]*3 for _ in range(n)]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + col[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + col[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + col[i][2]
    return min(dp[n-1])

print(sum(n))