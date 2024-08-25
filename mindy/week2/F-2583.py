from collections import deque

m,n,k = map(int, input().split())

# visited를 두어 true인 곳 count 하기
# 첫줄부터 바꿔서 해당 영역 1로 채우기

visited = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(min(y1, y2), max(y1, y2) ):
        for j in range(min(x1, x2), max(x1, x2)):
            visited[i][j] += 1
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    

    
def dfs(x,y):
    global count
    queue = deque()
    queue.append((x, y))
    count=1

    while queue:
        
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny]=1
                queue.append((nx, ny))
                count +=1
    return count

regions = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j]+=1
            region_size = dfs(i, j)
            regions.append(region_size)
    
    
regions.sort()
print(len(regions))
for i in regions:
    print(i,end=' ')