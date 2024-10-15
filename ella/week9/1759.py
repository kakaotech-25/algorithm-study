# 암호는 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
import sys
input = sys.stdin.readline
l, c = map(int, input().split())
arr = list(map(str, input().split()))
answer = []
vowel = ['a', 'e', 'i', 'o', 'u']

arr.sort()

def back():
    if len(answer) == l:
        cnt = 0
        for i in answer:
            if i in vowel:
                cnt += 1
        if cnt >= 1 and l - cnt >= 2:
            print(*answer, sep='')
        return
    else:
        for i in arr:
            if len(answer) == 0 or i > answer[-1]:
                answer.append(i)
                back()
                answer.pop()
back()