import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

m = int(input())
arr = list(map(int, input().split()))

answer = [0 for _ in range(m)]

card.sort()

def binary(t, s, e):
    global flag
    while s <= e:
        mid = (e + s) // 2
        if card[mid] == t or card[e] == t or card[s] == t:
            flag = True
            break
        if card[mid] > t:
            e = mid - 1
        if card[mid] < t:
            s = mid + 1

for i in range(m):
    flag = False
    binary(arr[i], 0, n-1)
    if flag == True:
        answer[i] = 1

print("\n".join(map(str, answer)))