'''
1: N K
    N: 온도를 측정한 전체 날짜의 수 (2 <= N <= 100000)
    K: 연속적인 날짜의 수 (1<k<N)
2: N개의 정수 빈 칸을 사이에 두고 주어짐
'''
N, K = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

s = [sum(t[:K])]
for i in range(1, N-K+1):
    s.append(s[i-1]- t[i-1] + t[i+K-1])

print(max(s))
