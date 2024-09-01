i, j = map(int, input().split(" ")) 
arr = [[-1 for _ in range(j)] for _ in range(i)]
for x in range(i):
    row = input()
    for y in range(j):
        if row[y] == "c":
            cnt = 0
            for k in range(y, j):
                arr[x][k] = cnt
                cnt += 1
            continue

for x in range(i):
    for y in range(j):
        print(arr[x][y], end=" ")
    print()
