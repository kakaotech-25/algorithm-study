# 5의 배수 개수 count
n = int(input())

for _ in range(n):
    s = int(input())
    cnt = 0
    i = 5
    while i<=s:
        cnt +=s//i
        i *=5
    print(cnt)