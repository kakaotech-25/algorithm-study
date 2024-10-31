# sum: 최종 합, k: 현재 인덱스
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def back(sum, k):
    global cnt

    if k >= n: # 정답
        return
    
    sum += arr[k] # 현재 인덱스 원소값을 더함
    if sum == s: # 위에서 더한 값이 s와 같은 경우
        cnt += 1 # 정답의 개수+1
    
    back(sum - arr[k], k+1) # 현재 인덱스를 포함하지 않는 경우
    back(sum, k+1) # 현재 인덱스를 포함하는 경우

back(0, 0)
print(cnt)