import sys

[n, arr, x] = sys.stdin.read().splitlines()

x = int(x)
arrList: list = list(arr.split(' '))
arrNumList = list(map(int, arrList))
arrNumList.sort()

count = 0
start = 0
end = len(arrNumList) - 1
while start < end:
    sum = arrNumList[start] + arrNumList[end]
    if sum == x:
        start += 1
        end -= 1
        count += 1
    elif sum < x:
        start += 1
    elif sum > x:
        end -= 1

print(count)
