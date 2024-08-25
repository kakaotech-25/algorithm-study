from collections import deque
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph=[]
ans =1
max_height = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))
    max_height = max(max_height, max(graph[-1]))
    
def bfs(x,y,r):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny] == 1 or graph[nx][ny] <= r:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1
            
for i in range(max_height):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y]>i and not visited[x][y]:
                cnt +=1
                
                bfs(x,y,i)
    ans = max(ans,cnt)

print(ans)