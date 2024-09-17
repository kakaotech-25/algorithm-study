'''
지렁이: 현재 위치 포함 인접한 1칸까지 배추 보호

'''
from collections import deque

T = int(input())
answer = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, visited, field):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            elif visited[ny][nx] or field[ny][nx] == 0:
                continue

            q.append((nx, ny))
            visited[ny][nx] = True

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    worm = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                bfs(j, i, visited, field)
                worm += 1
    
    answer.append(worm)

for i in range(T):
    print(answer[i])