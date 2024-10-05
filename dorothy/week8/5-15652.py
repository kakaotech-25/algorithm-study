from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().strip().split())
c = combinations_with_replacement([str(x+1) for x in range(n)], m)
for e in c:
    print(" ".join(e))