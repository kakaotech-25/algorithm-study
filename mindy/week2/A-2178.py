# bfs -> 주로 큐로 구현
# 가장 가까운 노드부터 탐색하고, 방문한 위치에 대해 거리를 누적
# bfs에서는 가장 먼저들어온 요소부터 처리하기 때문에 탐색이 너비 우선으로 이루어짐 
# 모든 경로를 같은 깊이로 동시에 탐색하기 때문에 도착점에 처음 도달하는 경로가 최단 경로임이 보장

from collections import deque

n, m = map(int, input().split())

graph = []

# n개의 리스트를 가진 미로
for _ in range(n):
    graph.append(list(map(int,input())))



def bfs(x,y):
    # 갈 수 있는 방향 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((x,y))
    
    # 큐가 빌때까지 반복문 수행
    while queue:
        # 큐의 가장 왼쪽에 있는 요소를 꺼내어 (x, y)에 할당
        x,y = queue.popleft()
        # 현재 위치에서 이동할 수 있는 새로운 위치 계산
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 위치를 벗어나거나 벽이 있는 경우 continue
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            # 새 위치가 길인 경우 graph[nx][ny]를 현재 위치에서 +1로 업데이트
            # 출발점에서 해당 위치까지의 이동거리를 나타냄
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
            