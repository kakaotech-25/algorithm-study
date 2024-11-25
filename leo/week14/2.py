# 항상 모든 간선이 비가중치이거나 가중치가 동일한 그래프에서의 최단 거리는 BFS로 구할 수 있음을 알고 있어야 합니다.

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
start, end = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, k = map(int, input().split())
    graph[a].append((b, k)) # 그래프 A 노드에 B로 가는 비용 적어놓기
    graph[b].append((a, k)) # 그래프 B 노드에 A로 가는 비용 적어놓기
    
dq = deque()
dq.append(start)
dist = [-1 for _ in range(N + 1)] # 간선에 도달했는지 체크하는 용도, -1이 미방문 + 비용 기입 
dist[start] = 1

while dq:
    cur = dq.popleft() # 큐에서 한개 꺼냄
    for next_node, k in graph[cur]: # 주변 탐색
        if dist[next_node] == -1 and dist[cur] <= k:
            dq.append(next_node) # 큐에 삽입
            dist[next_node] = dist[cur] + 1 #비용 업데이트

print(dist[end]) # 와 실패하는 경우 -1 에러처리까지 한꺼번에? 대체 어디까지 보고 짜는거임
