'''
체력 (i-1) % 4 + 1 까임
체력 0 이하일 때 쓰러짐
권총을 발사해야 하는 횟수
0 1 2 3
1 3 2 4
1 2 3 4
'''
import sys
n = int(sys.stdin.readline().strip())
h = [int(x) for x in sys.stdin.readline().strip().split()]

cnt = 0

for e in h:
	remain = e % 10
	cnt += (e // 10) * 4
	if remain > 0:
		for i in range(4):
			cnt += 1
			remain -= ((cnt-1) % 4) + 1
			if remain <= 0:
				break

print(cnt)