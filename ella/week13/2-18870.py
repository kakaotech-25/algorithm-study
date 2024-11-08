#이분탐색으로 안풀었음,,
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

d = defaultdict(int) #리스트값(key)이 음수거나 10^6 이상일 경우 딕셔너리를 씀

cnt = 0
answer = []

sortX = sorted(set(x)) #중복제거 -> 정렬(순서 중요! set은 순서 보장X)

for i in sortX:
    d[i] = cnt
    cnt += 1

for i in x:
    answer.append(d[i])

print(*answer)