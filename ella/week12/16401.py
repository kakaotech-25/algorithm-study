import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snack = list(map(int, input().split()))

snack.sort()

def back(l, h):
    if l > h:
        print(h)
        return
    sum = 0
    mid = (l + h) // 2
    for i in snack:
        sum += (i // mid)
    if sum < m:
        h = mid - 1
        back(l, h)
    if sum >= m:
        l = mid + 1
        back(l, h)

back(1, max(snack))