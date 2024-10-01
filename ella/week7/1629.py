# 백로그
# 분할정복을 이용한 거듭제곱
# a^b에서 b가 짝수일 경우: a^(n/2) * a^(n/2)
# a^b에서 b가 홀수일 경우: a^((n-1)/2) * a^((n-1)/2) * a
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def squ(a, b):
    if b == 1:
        return a % c
    else:
        x = squ(a, b//2)
        if b%2 == 0:
            return (x * x) % c # b가 짝수일 경우
        else:
            return (x * x * a) % c # b가 음수일 경우
        
print(squ(a, b))