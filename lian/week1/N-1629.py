# 지수 법칙 : A^m+n = A^m x A^n
# 나머지 분배 법칙 : (AxB)%C = (A%C) *(B%C) % C

A, B, C = map(int, input().split())

def dac(a, b, c):
    if b == 1:
        return a % c
    else:
        tmp = dac(a, b//2, c)
        if b % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp**2 * a % c
print(dac(A,B,C))