#BFS
#백로그
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, k = map(int, input().split())
    graph[a].append((b, k))
    graph[b].append((a, k))

def bfs(s, graph):
    queue = deque()
    queue.append(s)
    dist = [-1] * (n + 1)
    dist[s] = 1

    while queue:
        cur = queue.popleft()

        for nxt, k in graph[cur]:
            if dist[nxt] == -1 and dist[cur] <= k:
                queue.append(nxt)
                dist[nxt] = dist[cur] + 1
    
    print(dist[e])

bfs(s, graph)