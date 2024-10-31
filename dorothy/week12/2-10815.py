import sys

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
ans = []

cards = sorted(cards)
# print(cards)

for i in nums:
    start = 0
    end = n-1
    pivot = n // 2
    flag = False
    while True:
        if cards[pivot] == i:
            flag = True
            break
        if cards[pivot] < i:
            start = pivot
        else:
            end = pivot

        n_pivot = (start + end) // 2
        if pivot == n_pivot:
            if cards[start] == i or cards[end] == i:
                flag = True
            else:
                flag = False
            break
        pivot = n_pivot
    
    if flag:
        ans.append("1")
    else:
        ans.append("0")

print(" ".join(ans))
