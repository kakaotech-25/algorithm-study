import sys

input = sys.stdin.readline

n = int(input())

def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)
    
print(2**n-1)
hanoi(n,1,3)