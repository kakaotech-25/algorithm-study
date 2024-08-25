#unsloved
from collections import deque

n = int(input())
loc = []
max = 0

for i in range(n):
    loc.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if loc[i][j] > max:
            max = loc[i][j]

def bfs(x, y, h):
    #상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((x,y))
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and ny>=0 and nx<n and ny<n:
                if visit[nx][ny] == 0 and loc[nx][ny] > h:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
result = 0           
for i in range(max): 
    visit =  [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if loc[j][k] > i and visit[j][k] == 0: 
                bfs(j, k, i)
                count += 1
    result = max(result, count)
print(count)
