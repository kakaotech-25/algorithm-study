'''
* N개의 자연수 중에서 M개를 고른 수열
* 고른 수열은 오름차순이어야 한다.
'''
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().strip().split())
nums = (int(x) for x in sys.stdin.readline().strip().split())
ans = combinations(nums, m)
ans = map(sorted, ans)
ans = sorted(ans)
for e in ans:
    print(" ".join(map(str, e)))