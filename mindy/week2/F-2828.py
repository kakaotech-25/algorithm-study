# continue : 하위 코딩을 건너뛰고 다음 순번의 loop를 수행한다.
# pass : 실행할 코드가 없는 것으로 다음 행동을 수행한다.
# break : 반복문을 멈추고 loop 밖으로 나간다

from collections import deque
# 입력받기

n, m = map(int, input().split())

j = int(input())

left=1
right = m
cnt = 0


for _ in range(j):
    apple = int(input())
    
    # 사과의 위치가 바구니 내에 있는 경우
    if left <= apple and right>=apple:
        continue
    # 사과의 위치가 바구니보다 왼쪽에 있는 경우
    elif left > apple:
        cnt += (left-apple)
        right -= (left-apple)
        left = apple
    # 사과의 위치가 바구니보다 오른쪽에 있는 경우
    else:
        cnt += (apple - right)
        left += (apple - right)
        right = apple
        
    
print(cnt)


