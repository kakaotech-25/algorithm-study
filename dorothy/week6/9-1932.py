'''
1. X가 3으로 나누어 떨어지면 3으로 나눈다
2. X가 2로 나누어 떨어지면 2로 나눈다
3. 1을 뺀다

연산을 사용하는 횟수의 최솟값

10 - 9 - 8
       - 3 - 1
   - 5 - 4


'''
import sys
N = int(sys.stdin.readline().strip())

def s(N):
    if N <= 1:
        return 0
    d1 = s(N//3) + N%3 + 1
    d2 = s(N//2) + N%2 + 1
    return min(d1, d2)

print(s(N))