import sys

input = sys.stdin.readline

n = int(input())
narr = list(map(int,input().split()))

m = int(input())
marr = list(map(int,input().split()))
narr.sort()


for i in marr:
    left, right =0, n-1
    tmp = 0
    while left<=right:
        mid = (left+right)//2
        if narr[mid] == i:
            tmp=1
            break
        elif narr[mid]<i:
            left = mid+1
        else:
            right = mid-1
    print(tmp)