# 시간초과 이슈로 visited 추가

import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
visited = [False]*n
chess=[0] * n

def check(row):
    for i in range(row):
        if chess[row] == chess[i] or row - i == abs(chess[row]-chess[i]):
            return False
    return True

def dfs(row):
    global cnt
    
    if row ==n:
        cnt+=1
        return
    
    for col in range(n):
        if visited[col]:
            continue
        chess[row]=col
        if check(row):
            visited[col]=True
            dfs(row+1)
            visited[col]=False
                


dfs(0)
print(cnt)