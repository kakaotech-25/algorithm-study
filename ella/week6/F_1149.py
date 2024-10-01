#백로그
import sys
input = sys.stdin.readline

n = int(input())
col = []
for i in range(n):
    col.append(list(map(int, input().split())))

def sum(n):
    dp = [[0]*3 for _ in range(n)]
    dp[0] = col[0] #첫행 설정

    # 이전 열에 같은 색상이 아닌 값 중 작은 값 + 현재 열 값
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + col[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + col[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + col[i][2]
    return min(dp[n-1]) # 총 합이 가장 작은 값 리턴

print(sum(n))