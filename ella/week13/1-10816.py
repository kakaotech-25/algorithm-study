#딕셔너리로 풀었음
#이분탐색으로는 아직,,
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
cardList = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

answer = []

cardList.sort()

d = defaultdict(int)

for i in cardList:
    d[i] += 1

for i in card:
    answer.append(d[i])

print(*answer)