# 백트래킹으로 풀면 Python3에서도 통과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()

def back(l, h):
    sum = 0
    mid = (l + h) // 2
    for i in range(n):
        x = tree[i] - mid
        if x > 0:
            sum += x
    if h < l:
        print(h)
        return
    if sum < m:
        h = mid - 1
        back(l, h)
    else:
        l = mid + 1
        back(l, h)

back(0, max(tree))