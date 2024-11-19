#백로그(다른 해설 참고)
#투포인터
import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))

left, right = 0, n-1 # 투포인터 설정
value = sys.maxsize # 가장 작은 절댓값을 찾기 위해 가장 큰 값으로 초기화
answer = []

while left < right:
    sum = liq[left] + liq[right] # 현재 포인터를 가리키는 숫자합
    if abs(sum) <= value: # 현재의 가장 작은 절댓값보다 숫자합 절대값보다 작을 경우
        answer = [liq[left], liq[right]] #정답 후보
        value = abs(sum) #가장 작은 절댓값 후보
    if sum < 0:
        left += 1 # 숫자합이 0보다 작을 경우 -> left포인터 증가
    elif sum > 0:
        right -= 1 #숫자합이 0보다 클 경우 -> right포인터 감소
    elif sum == 0:
        break #숫자합이 0일 경우 -> 너가 정답이여

print(*answer)