# 파이썬에 있는 collections 모듈의 counter 사용
# counter는 list의 안의 내용을 key,빈도수를 dictionary 형태로 저장해줌
# most_common : 가장 많이 등장한 순서대로 저장 [(,),(,)...] 꼴로 출력해줌

import collections
n,c=map(int,input().split())


message = list(map(int, input().split()))

frequency = collections.Counter(message)

f=frequency.most_common()

for key,value in f:
    for _ in range(value):
        print(key, end=' ')
        
