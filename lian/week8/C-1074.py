import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())

ans = 0
while n != 0:
    n -= 1
    size = 2**n
    
    if r < size and c < size:
        ans += 0
    elif r < size and c >= size:
        ans += size*size
        c -= size
    elif r >= size and c < size:
        ans += 2*size*size
        r -= size
    else:
        ans += 3*size*size
        r -= size
        c -= size
print(ans)