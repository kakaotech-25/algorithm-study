# unsolved
# 내구도, 무게
# 반대 계란의 무게만큼 계란 내구도 감소
import sys
input = sys.stdin.readline

n = int(input())
s = []
w = []
cnt = 0
arr = []

for i in range(n):
    si, wi = map(int, input().split())
    s.append(si)
    w.append(wi)

def back(k):
    global cnt
    if k >= n:
        return
    for i in range(k, n):
        if w[k] > s[i]:
            cnt += 1
            s[i] = 0
            back(k+1)
            break

back(0)
print(cnt)