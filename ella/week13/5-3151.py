# 백로그
# 투포인터
# 투포인터에 종류 2개
# 1. 연속된 배열 합 찾기 -> 정렬X
# 2. 2개의 값 합 찾기 -> 정렬O
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()
cnt = 0

def binary(t, start, end):
    global cnt
    max = n #중복값의 마지막 위치 저장, 가장 큰 인덱스 값으로 설정
    while start < end:
        sum = a[start] + a[end]
        if sum < t: #target값이 sum보다 클 경우
            start += 1 #start 포인터 증가 -> sum값 증가

        elif sum == t: #target값이 sum과 같을 경우
            if a[start] == a[end]: # a[start]와 a[end] 값이 같을 경우
                cnt += end - start # 사이값이 a[start]와 a[end]랑 모두 같아서 다 카운트
            else: # a[start]와 a[end] 값이 다를 경우
                if max > end: #end값이 가장 큰 인덱스 값보다 작을 경우(중복값 처리)
                    max = end #중복값 위치 갱신
                    while max >= 0 and a[max - 1] == a[end]: #a[end]이 이전 값들과 동일할 경우 값을 건너뛰기위해 max갱신
                        max -= 1
                cnt += end - max + 1 #max값 이후와 end 값까지 유효한 값
            start += 1 #start 포인터 증가 -> 다음 후보 찾기

        elif sum > t: #target값이 sum보다 작을 경우
            end -= 1 #end값 포인터 감소 -> sum값 감소

for i in range(n - 2):
    start = i + 1
    end = n - 1
    target = -a[i]
    binary(target, start, end)

print(cnt)