'''
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
'''
import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().strip().split())
nums = (int(x) for x in sys.stdin.readline().strip().split())
nums = combinations_with_replacement(nums, m)
nums = map(sorted, nums)
nums = sorted(nums)
for e in nums:
    print(" ".join(map(str, e)))