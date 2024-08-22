# bfs
from collections import deque
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 # 시작점을 방문 했다고 친다 
    
    # 인접한 모든 1을 탐색하면서 0으로 변경
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx >=m or ny<0 or ny >=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return

# k개의 좌표를 받아 그 위치들을 다 1로 지정
for _ in range(t):
    m, n, k = map(int, input().split())
    graph =[[0]*(n) for _ in range(m)]

    for j in range(k):
        x, y = map(int,input().split())
        graph[x][y]=1
    cnt=0
    # 2중 for문으로 모든 위치 탐색
    # 모든 좌표를 탐색하며 1인 경우 0으로 변경
    for a in range(m):
        for b in range(n):
            if graph[a][b]==1:
                bfs(graph,a,b)
                cnt+=1
                
    print(cnt)