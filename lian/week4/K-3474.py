n = int(input())
for _ in range(n):
    tmp = int(input())
    ans = 0
    num = 5
    while num <= tmp:
        ans += tmp//num
        num *= 5
    print(ans)