import sys
input = sys.stdin.readline

N, S = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]

tmp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
	for j in range(1, N+1):
		tmp[i][j] = tmp[i-1][j] + tmp[i][j-1] - tmp[i-1][j-1] + ls[i-1][j-1]
		
def check(K):
	for i in range(1, N-K+2):
		for j in range(1, N-K+2):
			num = tmp[i+K-1][j+K-1] - tmp[i-1][j+K-1] - tmp[i+K-1][j-1] + tmp[i-1][j-1]
			if num < S:
				return False
	return True

start, end = 1, N
ans = -1

while start <= end:
	mid = (start+end)//2
	if check(mid):
		ans = mid
		end = mid-1
	else:
		start = mid+1
print(ans)