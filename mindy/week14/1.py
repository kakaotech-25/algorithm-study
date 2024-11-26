# set에는 remove, add 사용하기..
import sys

input = sys.stdin.readline

n , m = map(int, input().split())

narr = set(map(str,input().split()))
marr = set(map(str,input().split()))

for _ in range(m):
	x,y = map(str, input().split())
	if x in narr and y in marr:
		narr.remove(x)
		marr.remove(y)
		
		narr.add(y)
		marr.add(x)
print(' '.join(sorted(narr)))