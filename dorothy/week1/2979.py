'''
트럭 3대
트럭 주차하는 데 필요한 총 비용
A원*1/min(1대)
B원*2/min(2대)
C원*3/min(3대)
1<=C<=B<=A<=100
'''

A, B, C = [int(fee) for fee in input().split()]
truck = [list(map(int, input().split())) for _ in range(3)]
t = [0] * 100

for i in truck:
    for j in range(i[0], i[1]):
        t[j]+=1

total_fee = t.count(1) * A * 1 + t.count(2) * B * 2 + t.count(3) * C * 3
print(total_fee)