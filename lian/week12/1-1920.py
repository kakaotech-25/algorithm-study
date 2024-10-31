import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

ls = sorted(ls)

for num in check:
    low, high = 0, len(ls) - 1
    tmp = 0
    while low <= high:
        mid = (low+high)//2
        if num < ls[mid]:
            high = mid-1
        elif num > ls[mid]:
            low = mid+1
        elif num == ls[mid] or num == ls[low] or num == ls[high]:
            tmp = 1
            break
    print(tmp)