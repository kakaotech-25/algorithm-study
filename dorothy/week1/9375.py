'''
1: 의상의 수 n (0<=n<=30)
2~: n개의 의상의 이름과 의상의 종류
'''
count = int(input())

results = []
for _ in range(count):
    n = int(input())
    wear = {}
    for _ in range(n):
        name, weartype = input().split()
        if weartype in wear:
            wear[weartype].append(name)
        else:
            wear[weartype] = [name]

    if len(wear):
        c = 1
        for val in wear.values():
            c *= len(val) + 1
        c -= 1
        results.append(c)
    else:
        results.append(0)

[print(x) for x in results]