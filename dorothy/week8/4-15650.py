from itertools import combinations
import sys
n, m = map(int, sys.stdin.readline().strip().split())
c = combinations([str(x+1) for x in range(n)], m)
# c = [sorted(e) for e in c]
for e in c:
    print(" ".join(e))