import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Nls = set()
Mls = set()

for i in input().split():
	Nls.add(i)
for i in input().split():
	Mls.add(i)

for _ in range(M):
	a, b = map(str, input().split())
	if a in Nls and b in Mls:
		Nls.remove(a)
		Nls.add(b)
		Mls.remove(b)
		Mls.add(a)
ans = sorted(list(Nls))
print(*ans)