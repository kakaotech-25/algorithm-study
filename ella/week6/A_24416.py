#python3 시간초과
#pypy3로 통과..
import sys
input = sys.stdin.readline
n = int(input())

cnt1 = 0
cnt2 = 0

# 재귀호출
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))

# 동적 프로그래밍(DP)
# Top-Down (메모이제이션 방식) - 재귀 사용
def fibonacci(n):
    global cnt2

    # 메모이제이션
    f = [0] * n # 피보나치 수열을 저장할 배열

    # 초기값 설정
    f[0] = 1
    f[1] = 1

    # 점화식
    # 피보나치 수열 계산
    for i in range(2, n):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n-1]

fib(n)
fibonacci(n)
print(cnt1, cnt2)