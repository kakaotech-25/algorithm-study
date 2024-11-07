import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input().strip())
cards = tuple(map(int, input().strip().split()))
m = int(input().strip())
nums = tuple(map(int, input().strip().split()))

d = defaultdict(int)

for card in cards:
    d[card] += 1

ans = []
for num in nums:
    ans.append(d[num])