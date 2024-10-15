import sys
from itertools import combinations

def gathers(s):
    cnt = 0
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    
    return cnt

def isValid(s, length):
    if gathers(s) >= 1 and gathers(s) < length - 1:
        return True
    return False

l, c = map(int, sys.stdin.readline().strip().split())
chars = sys.stdin.readline().strip().split()
ans = combinations(chars, l)
ans = map(sorted, ans)
ans = sorted(ans)
for e in ans:
    if isValid(e, l):
        print("".join(e))