import math

cards: str = input()
arr: list = [0 for _ in range(10)]

for i in cards:
    if int(i) == 6 or int(i) == 9:
        arr[6] += 1
    else :
        arr[int(i)] += 1

arr[6] = math.ceil(arr[6] / 2)

result = 0
for i in arr:
    result = max(result, i)

print(result)
    
