import sys
input = sys.stdin.readline

def star(n):
    if n == 1:
        return '*'
    stars = star(n//3)
    ans = []

    for i in stars:
        ans.append(i*3)
    for i in stars:
        ans.append(i + ' '*(n//3) + i)
    for i in stars:
        ans.append(i*3)
    return ans

N = int(input())
ans = star(N)
for i in ans:
    print(i)