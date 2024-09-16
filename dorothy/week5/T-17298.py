'''
NGE(i): 오른쪽에 있으면서 A_i보다 큰 수 중에서 가장 왼족에 있는 수. 그러한 수가 없으면 -1
ex)
A=[3, 5, 2, 7]
NGE(1)=5
NGE(2)=7
NGE(3)=7
NGE(4)=-1

1: len(A)=N
2: A1, A2, ..., AN
출력: NGE(1), NGE(2), ..., NGE(N)

삽질방지 팁
- 파이썬 슬라이싱은 배열을 복사해서 새로운 배열을 만드는 거기 때문에 시간 초과가 날 수 있음
- 엥? 근데 이중 for 문은 시간 초과가 납니다링
'''
N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        NGE[idx] = A[i]
    stack.append(i)

print(" ".join(list(map(str, NGE))))