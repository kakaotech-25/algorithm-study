import sys

n = int(sys.stdin.readline().strip())
a = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())

a = sorted(a)
for i in nums:
    low = 0
    high = n-1
    tmp = 0
    while low <= high:
        mid = (low + high) // 2
        if a[mid] > i:
            high = mid - 1
        elif a[mid] < i:
            low = mid + 1
        elif i in (a[low], a[high], a[mid]):
            tmp = 1
            break
    print(tmp)