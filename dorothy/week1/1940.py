'''
1: 재료의 개수 N(1<=N<=15000)
2: 갑옷을 만드는 데 필요한 수 M(1<=M<=10000000)
3: N개의 재료가 가진 고유한 번호
재료의 고유한 번호 2개 합쳐서 M이 되면 갑옷을 만들 수 있음.
'''
N = int(input())
M = int(input())
materials = [int(x) for x in input().split()]

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if materials[i]+materials[j] == M:
            cnt += 1

print(cnt)