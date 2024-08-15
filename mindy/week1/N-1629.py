# 분할 정복 문제
# 거듭제곱을 계산할 떄 지수를 반씩 줄여나가 계산속도 향상
# Daq(2,5) -> Daq(2,2) -> Daq(2,1)
# 2 -> 2*2%1000 -> 4*4%2%1000 -> 32*32%1000
# 시간 복잡도 O(log b)

import sys

input = sys.stdin.readline

a,b,c = map(int, input().strip().split())

def Daq(a,b):
    if b==1: # b가 1이 될때까지 재귀
        return a%c
    else:
        tmp = Daq(a,b//2)
        if b%2 == 0:
            return tmp * tmp %c
        else:
            return tmp * tmp * a %c
        

re = Daq(a,b)
print(re)
