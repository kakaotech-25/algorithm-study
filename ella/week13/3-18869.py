#unsolved
#똥코드,,아직 못풀었습니다,,ㅈㅅ
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
for i in range(m):
    planet = list(map(int, input().split()))
    x = sorted(planet)
    lis = []
    cnt = 0
    for j in range(n):
        lis.append(cnt)