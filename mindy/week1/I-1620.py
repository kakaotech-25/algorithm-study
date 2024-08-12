# list로 풀었더니 계속 시간초과가 발생하여 dictionary로 변경

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

"""pkm = [input().strip() for __ in range(n)]

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(pkm[int(q)-1])
    else:
        print(pkm.index(q)+1)"""

dic={}

for i in range(1,n+1):
    a = input().strip()
    dic[i]=a
    dic[a] =i

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])

