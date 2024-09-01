# 비내림차순을 찾는 문제
# 다음 수가 앞의 수보다 크거나 같은경우
# 없으면 0 출력
# 숫자만 출력하고 내림차순으로 sort한 후 출력

import re

result = []
n = int(input())

for _ in range(n):
    text = input()
    numbers = re.split(r'\D+',text)
    for number in numbers:
        if number != '':
            result.append(int(number))

result.sort(reverse=False)

for i in result:
    print(i)