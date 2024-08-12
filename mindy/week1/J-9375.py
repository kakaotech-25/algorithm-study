# 조합 사용
# 각 조합을 1개만 하는 경우도 고려해야하기 때문에 +1
# 마지막으로 알몸인 경우는 제외하므로 -1
# dictionary의 요소로 list 사용가능하므로 append

import sys

input = sys.stdin.readline


n = int(input().strip())
for i in range(n):
    dic=dict()
    m = int(input().strip())
    for _ in range(m):
        a, b = input().strip().split()
        if b in dic:
            dic[b].append(a)
        else:
            dic[b]=[a]
    

    cnt=1
    for k in dic:
        cnt *= (len(dic[k])+1)

    print(cnt-1)