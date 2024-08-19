N, M = map(int, input().split())
# N = 도감에 수록되어 있는 포켓몬 수 / M = 내가 맞춰야 하는 문제의 개수
pkm_int = {}
pkm_str = {}
for i in range(N):
    tmp = input()
    pkm_int[i+1] = tmp
    pkm_str[tmp] = i+1
for _ in range(M):
    quiz = input()
    if str.isdigit(quiz): #정수일 때 True를 반환해주는 함수
        print(pkm_int[int(quiz)])
    else:
        print(pkm_str[quiz])