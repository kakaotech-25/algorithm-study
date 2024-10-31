from itertools import combinations_with_replacement

n, m = map(int, input().split())
c = map(int, input().split())
c = combinations_with_replacement(c, m)
c = sorted(map(tuple,(map(sorted, c))))
c = sorted(set(c))

for e in c:
    print(" ".join(map(str, e)))