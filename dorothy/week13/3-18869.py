import sys
import math
from collections import defaultdict

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
s = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
d = defaultdict(int)

for space in s:
    sorted_space = sorted(space)
    rank = {sorted_space[x]: x for x in range(n)}
    vector = tuple([rank[x] for x in space])
    d[vector] += 1

sum = 0
for i in d.values():
    sum += math.comb(i, 2)

print(sum)