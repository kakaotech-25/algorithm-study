# unsolved
# 0의 개수 -> 10이 곱해진 횟수
# 10 = 2*5 -> 2의 배수나 5의 배수의 개수를 구하면 된다!
# 5가 2보다 더 크기때문에 5의 베수 개수 구하기

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    num = 5 # 5의 배수
    while num <= n: # num이 n보다 작은 경우
        cnt += n // num # 5의 배수로 나눈 몫이 5의 배수 개수
        num *= 5 # 5^2, 5^3 ... < n
    print(cnt)