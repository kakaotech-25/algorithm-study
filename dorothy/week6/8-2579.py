'''
1. 계단은 한 번에 한 계단씩 또는 두 계단식 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
'''
import sys
n = int(sys.stdin.readline().strip())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]

def s(c, warning=0):
    if c >= n - 1:
        return stairs[n-1]
    d2 = s(c+2, warning=0) + stairs[c]
    if warning >= 2 or c >= n-3:
        print(d2)
        return d2
    d1 = s(c+1, warning=warning+1) + stairs[c]
    print(max(d1, d2))
    return max(d1, d2)

print(s(-1))