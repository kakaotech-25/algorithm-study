from itertools import combinations

L, C = map(int, input().split())
ls = sorted(list(map(str, input().split())))

vowels = ['a', 'e', 'i', 'o', 'u']

for i in combinations(ls, L):
    cnt_v = 0
    cnt_c = 0

    for c in i:
        if c in vowels:
            cnt_v += 1
        else:
            cnt_c += 1
    
    if cnt_v >= 1 and cnt_c >= 2:
        print(''.join(i))
