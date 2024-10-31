#unsolved
#퀸: 위, 아래, 대각선으로 움직일 수 있음
#서로 공격하지 못하게 할려면 대각선

#행(row), 열(col)
#대각선(dia): 왼쪽 대각선(row-col), 오른쪽 대각선(row+col)
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
cnt = []

def back():
    global answer
    if len(cnt) == n:
        answer += 1
        return

    for i in range(n):
        if i not in cnt:
            cnt.append(i) 
            back() 
            cnt.pop()

back()
print(answer)
