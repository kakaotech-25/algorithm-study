# 브루트 포스 알고리즘(완전 탐색 알고리즘)

n = int(input())
num = 666 # 첫번재 영화 숫자
cnt = 0 # 666이 들어가는 숫자 count

while True:
    if "666" in str(num): # 연속 666이 있어야 함, 없을 경우 count X
        cnt += 1
    if cnt == n: # n번째 영화 숫자까지 count해서 반복문 탈출
        break
    num += 1

print(num)