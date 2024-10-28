from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
c = combinations(nums, m)
c = map(tuple, map(sorted,c))
# print(c)
c = set(c)
c = sorted(c)

for e in c:
    print(" ".join(map(str, e)))