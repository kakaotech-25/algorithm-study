import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lines = tuple(tuple(map(int, input().split())) for _ in range(N))
B = lines
def 구간합_구하는_함수(i1, i2, j1, j2):
    sum = B[i2][j2] - B[i1 - 1][j2] - B[i2][j1 - 1] + B[i1 - 1][j1 - 1]
    return sum

def 누적합_채워넣는_함수():
    
print(lines)