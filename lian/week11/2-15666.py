import sys
input = sys.stdin.readline

def dfs(N, M, start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    tmp = 0
    for i in range(start, N):
        if tmp != nums[i]:
            dfs(N, M, i, path + [nums[i]])
            tmp = nums[i]

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
dfs(N, M, 0, [])
