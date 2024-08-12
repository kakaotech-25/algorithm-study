a, b, c = map(int, input().split())
arr = [0]*100
ans = 0
for _ in range(3):
    enter, out = map(int, input().split())
    for i in range(enter, out):
        arr[i] += 1

for j in arr:
    if j == 1:
        ans += a
    elif j == 2:
        ans += b*2
    elif j == 3:
        ans += c*3
print(ans)