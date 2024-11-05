import sys
input = sys.stdin.readline

# na, nb = map(int, input().strip().split())
# a = set(map(int, input().strip().split()))
# b = set(map(int, input().strip().split()))

# ans = a - b
# ans = sorted(ans)
# print(len(ans))
# print(*ans)

na, nb = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
b = sorted(b)
ans = []

for i in a:
    low = 0
    high = nb-1
    flag = True
    while low <= high:
        mid = (low + high) // 2
        if i < b[mid]:
            high = mid - 1
        elif i > b[mid]:
            low = mid + 1
        elif i in (b[mid], b[high], b[low]):
            flag = False
            break
    if flag:
        ans.append(i)

print(len(ans))
ans = sorted(ans)
if ans:
    print(*ans)