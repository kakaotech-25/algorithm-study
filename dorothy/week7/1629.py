'''
궁금한 점: 전체 결과에서 나머지 연산을 하면 시간 초과가 뜨는데, return 단계에서 나머지 연산을 하니 시간 초과가 뜨지 않음. 왜일까요?
'''

import sys
a, b, c = map(int, sys.stdin.readline().strip().split())

def s(a, b):
    if b == 1:
        return a % c
    return (s(a, b//2) ** 2) * (a ** (b % 2)) % c
    

print(s(a, b))