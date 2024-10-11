import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def back():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    else:
        for i in range(1, n+1):
            if len(arr) == 0 or i >= arr[-1]: #증가 순서 확인
                arr.append(i)
                back()
                arr.pop()
back()