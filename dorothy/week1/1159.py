'''
첫 번째 글자가 같은 선수 5명을 선발
5명보다 적다면 기권
뽑을 수 있는 성의 첫 글자를 모두 구한다.

1: 선수의 수 N
2~: N개의 줄, 각 선수의 성 (<=30) (1<=N<=150)
'''

N = int(input())
players = [input() for _ in range(N)]
cnt = [0] * 26

for p in players:
    cnt[ord(p[0]) - ord('a')] += 1

ans = ""

for i in range(26):
    if cnt[i] >= 5:
        ans += chr(i + ord('a'))

if len(ans) != 0:
    print(ans)
else:
    print("PREDAJA")