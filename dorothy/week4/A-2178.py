'''
1=이동할 수 있는 칸
0=이동할 수 없는 칸

(1,1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
'''
import sys
from collections import deque

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
INF = N * M

q = deque()
q.append((1, 1))

while q:
    x, y = q.popleft()
    
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if n_x <= 0 or n_x > M or n_y <= 0 or n_y > N:
            continue
        elif visited[n_y - 1][n_x - 1] or maze[n_y - 1][n_x - 1] == 0:
            continue

        visited[n_y - 1][n_x - 1] = True
        q.append((n_x, n_y))
        maze[n_y - 1][n_x - 1] = maze[y - 1][x - 1] + 1

# 우, 하
print(maze[N - 1][M - 1])
