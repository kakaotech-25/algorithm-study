import sys
input = sys.stdin.readline

def dfs(N, M, start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for i in range(start, N+1):
        dfs(N, M, i, path+[i])

N, M = map(int, input().split())
dfs(N, M, 1, [])
