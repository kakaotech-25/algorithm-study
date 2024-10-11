#백로그
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def back():
    if len(arr) == m: #배열 길이(정답)
        print(" ".join(map(str, arr)))
        return
    else: #정답이 아닐 경우
        for i in range(1, n+1): #모든 자식 노드
            if i not in arr and (len(arr) == 0 or i > arr[-1]): #중복 확인 및 증가 순서 확인(정답 후보)
                arr.append(i)
                back()
                arr.pop()
back()