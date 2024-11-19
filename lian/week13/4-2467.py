import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int, input().split()))

low, high = 0, N - 1
now = ls[low] + ls[high]
tmp = abs(now)
ans = [ls[low], ls[high]]

while low < high:
    now = ls[low] + ls[high]
    if abs(now) < tmp:
        tmp = abs(now)
        ans = [ls[low], ls[high]]
    
    if now < 0:
        low += 1
    elif now > 0:
        high -= 1
    else:
        break
print(ans[0], ans[1])