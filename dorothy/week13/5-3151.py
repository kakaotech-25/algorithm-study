from itertools import combinations
import sys
import bisect

input = sys.stdin.readline
n = int(input().strip())
s = tuple(map(int, input().strip().split()))
s = tuple(sorted(s))
ans = 0

for i in range(n-1):
    for j in range(1, n):
        tmp = -(s[i]+s[j])
        ans += bisect.bisect_right(s, tmp, i+1, j) - bisect.bisect_left(s, tmp, i+1, j)

print(ans)