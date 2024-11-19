import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
ls = list(map(int, input().split()))
ls.sort()
cnt = 0

for i in range(N - 2):

    if ls[i] > 0:
        break
    
    low, high = i+1, N-1
    while low < high:
        tmp = ls[i] + ls[low] + ls[high]
        if tmp == 0:
            if ls[low] == ls[high]:
                cnt += (high-low+1) * (high-low) // 2
                break
            else:
                low_cnt, high_cnt = 1, 1
                while low+1 < high and ls[low] == ls[low+1]:
                    low += 1
                    low_cnt += 1
                while high-1 > low and ls[high] == ls[high-1]:
                    high -= 1
                    high_cnt += 1
                cnt += low_cnt * high_cnt
                low += 1
                high -= 1
        elif tmp < 0:
            low += 1
        else:
            high -= 1
print(cnt)