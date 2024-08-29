check = int(input())
title = 666
ans = 0

while True:
    if '666' in str(title):
        ans += 1
        if ans == check:
            print(int(title))
            break
    title += 1