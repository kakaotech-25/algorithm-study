import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int, input().split()))
sorted_ls = sorted(set(ls))
ans = []

for num in ls:
    low, high = 0, len(sorted_ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_ls[mid] < num:
            low = mid + 1
        elif sorted_ls[mid] > num:
            high = mid - 1
        else:
            ans.append(mid)
            break
print(*ans)