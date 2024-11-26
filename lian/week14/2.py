import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())  # N = 통신탑의 개수, M = 통신 케이블의 개수
S, E = map(int, input().split())  # S = 시작 통신탑 번호, E = 도착 통신탑 번호
ls = defaultdict(list)

for _ in range(M):
	a, b, k = map(int, input().split())
	ls[a].append((b, k))
	ls[b].append((a, k))

q = deque()
q.append((S, 1))
visited = [False] * (N+1)
visited[S] = True

flag = False
ans = -1

while q:
	now, data = q.popleft()
	for nxt, k in ls[now]:
		if not visited[nxt] and data <= k:
			visited[nxt] = True
			q.append((nxt, data + 1))
			if nxt == E:
				ans = data + 1
				flag = True
				break
	if flag:
		break

print(ans)
