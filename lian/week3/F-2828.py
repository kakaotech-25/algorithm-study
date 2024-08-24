N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for i in range(J)]
now = 1
ans = 0
for i in apples:
    if now <= i and i <= (now+M-1):
        continue
    elif i < now: #현재 위치보다 사과가 왼쪽에 있는 경우
        ans += now-i
        now = i
    else: #현재 위치보다 사과가 오른쪽에 있는 경우
        move = i - (now+M-1)
        ans += move
        now += move
print(ans)
