import sys
input = sys.stdin.readline

def hanoi(N, start, end):
    if N == 1:
        print(start, end)
        return
    tmp = 6-start-end
    hanoi(N-1, start, tmp)
    print(start, end)
    hanoi(N-1, tmp, end)

N = int(input())
print(2**N-1)
hanoi(N,1,3)