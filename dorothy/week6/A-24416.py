'''
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}

1: n (5<=n<=40)

3 -> 2 -> 1
          1
     1

7 -> 6 -> 5 -> 4 -> 3 -> 2
                      -> 1 
                 -> 2
            -> 3 -> 2
                    1
          4 -> 3 -> 2
                    1
     5 -> 4 -> 3 -> 2
            -> 2
          3 -> 2
            -> 1

3: f(1) + f(2) = 2
4: f(2) + f(3) - 1 = 3
5: f(3) + f(4) - 1 = 5
6: f(5) + f(4) - 1 = 7
7: f(6) + (f(5) - 1)

'''
import sys
n = int(sys.stdin.readline().strip())

def f(n):
    memo = [0] * (n + 1)
    memo[3] = 2
    memo[4] = 3

    for i in range(5, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

print(f(n), n-2)