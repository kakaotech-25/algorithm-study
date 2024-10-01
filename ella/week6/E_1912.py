import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def sum(n):
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    return max(dp)

print(sum(n))