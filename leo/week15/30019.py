import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())

arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

# 예약시스템 기록의 룸 번호를 키로 해서 start, end를 가지고 있을 딕셔너리 초기화
book = defaultdict(int)

for el in arr:
    room_number = el[0]
    start = el[1]
    end = el[2]
    # 만약 룸넘버가 예약되어있다면 start, end조건 계산
    if room_number in book:
        [prev_start, prev_end] = book.get(room_number)
        # 이전 예약보다 뒤인경우
        if start >= prev_end:
            book[room_number] = [prev_start, end]
            print('YES')
        # 이전 예약보다 앞인경우
        elif end <= prev_start:
            book[room_number] = [start, prev_end]
            print('YES')
        # 예약이 겹친 경우
        else:
            print('NO')
    # 룸넘버가 예약되어있지 않다면 예약
    else:
        book[room_number] = [start, end]
        print('YES')
 
        


