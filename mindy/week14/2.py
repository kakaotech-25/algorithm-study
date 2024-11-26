import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
	a, b,k=(map(int, input().split()))
	graph[a].append((b,k))
	graph[b].append((a,k))
	
dq =deque()
dq.append(s)
visit = [-1] * (n+1)
visit[s]=1

while dq:
	cur =dq.popleft()
	for nxt, k in graph[cur]:
		if visit[nxt]==-1 and visit[cur]<=k:
			dq.append(nxt)
			visit[nxt]=visit[cur]+1
			
print(visit[e])