'''
집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.
'''
import sys
from itertools import combinations
t = sys.stdin.readline().strip()
s = []
while t != "0":
    s.append(list(map(int, t.split())))
    t = sys.stdin.readline().strip()

for l in s:
    l = l[1:]
    # print(l)
    ans = combinations(l, 6)
    ans = map(sorted, ans)
    ans = sorted(ans)
    for e in ans:
        print(" ".join(map(str, e)))
    print()