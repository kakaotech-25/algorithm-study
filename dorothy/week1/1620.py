'''
1: N M (1 <= N, M <= 100000)
2~: N개의 줄에 포켓몬 번호 1~N 하나씩. 첫 글자만 대문자, 나머지는 소문자 or 마지막 문자만 대문자
2 <= len <= 20
?~: M개의 줄에 맞춰야 하는 문제.
'''
N, M = [int(x) for x in input().split()]
pokemon_list = [input() for _ in range(N)]
pokemon_dict = {}
for i in range(N):
    pokemon_dict[pokemon_list[i]] = i+1
question = [input() for _ in range(M)]

for q in question:
    if q.isdigit():
        print(pokemon_list[int(q)-1])
    else:
        print(pokemon_dict[q])
