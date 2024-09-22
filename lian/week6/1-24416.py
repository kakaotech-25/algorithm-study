#python 시간초과 나서 pypy로 돌림

n = int(input())
ans1 = 0
ans2 = 0

def fib(n):
    global ans1
    if n == 1 or n == 2:
        ans1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global ans2
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        ans2 += 1
    return f[n]
fib(n)
fibonacci(n)
print(ans1, ans2)