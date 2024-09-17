# 기본값을 가지는 딕셔너리를 만들어주는 defaultdict 라는 함수가 있음
# 평소처럼 그냥 큐를 리스트로 선언해서 사용하니 시간초과가 났다, deque를 사용하는 습관을 만들어야겠다
# bfs로 했는데도 시간초과 난다,,
# python으로 모든걸해봐도 시간초과가 난다면 pypy로 제출해보자! 

from collections import defaultdict, deque


N, M = map(int, input().split())
dic = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    dic[B].append(A)

def bfs(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] = True
    cnt = 1

    while q:
        check = q.popleft()
        for i in dic[check]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

ans = []
max_num = 0

for i in range(1, N+1):
    tmp = bfs(i)
    if tmp > max_num:
        max_num = tmp
        ans = [i]
    elif tmp == max_num:
        ans.append(i)

ans.sort()
print(*ans)
