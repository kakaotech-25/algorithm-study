#unsolved
#Timeout
import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
answer = 0
cnt = 1

for i in range(n):
	while h[i] > 0:
		h[i] = h[i] - (((cnt-1) % 4) + 1)
		answer += 1
		cnt += 1
		if h[i] <= 0:
			break
		
print(answer)