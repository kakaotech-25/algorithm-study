#set
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
aItems = set(input().split())
bItems = set(input().split())

for i in range(m):
    a, b = input().split()
    if a in aItems and b in bItems:
        aItems.remove(a)
        bItems.remove(b)
        aItems.add(b)
        bItems.add(a)

sorted_aItems = sorted(aItems)
print(*sorted_aItems)