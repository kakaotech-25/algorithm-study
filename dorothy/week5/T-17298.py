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
- 그치만 아직 못 풀었어요, 서울 가서 풀어야지.
'''
N = int(input())
A = list(map(int, input().split()))
NGE = []
for i in range(N):
    found = False
    for j in range(i, N):
        if A[j] > A[i]:
            NGE.append(A[j])
            found = True
            break
    if not found:
        NGE.append(-1)

# print(NGE)
# answer = []
# for i in range(1, N+1):
#     answer.append(str(NGE[i]))

print(" ".join(list(map(str, NGE))))