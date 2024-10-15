import sys
input = sys.stdin.readline

def dfs(ls, M, start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for i in range(start, len(ls)):
        dfs(ls, M, i, path + [ls[i]])

N, M = map(int, input().split())
ls = sorted(list(map(int, input().split())))
dfs(ls, M, 0, [])
