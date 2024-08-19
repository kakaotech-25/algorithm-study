'''
* sum(real_height) == 100
* 가능한 정답이 여러가지: 아무거나 출력
* 9명 중 7명
'''
import itertools

heights = [int(input()) for _ in range(9)]

for i in itertools.combinations(heights, 7):
    n = sum(i)
    if n == 100:
        for e in sorted(i):
            print(e)
        break
