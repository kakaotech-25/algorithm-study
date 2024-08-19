while True:
    try:
        n = int(input())
        ans = 1
        num = 1
        while True:
            if num % n == 0:
                break
            num = num * 10 + 1
            ans += 1
        print(ans)
    except:
        break