import sys
input = sys.stdin.readline

a, b = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
answer = []

listA.sort()
listB.sort()

def back(t, start, end):
    mid = (start + end) // 2
    if start > end:
        answer.append(t)
        return
    if t == listB[mid] or t == listB[end] or t == listB[start]:
        return
    if t > listB[mid]:
        start = mid + 1
        back(t, start, end)
    if t < listB[mid]:
        end = mid - 1
        back(t, start, end)

for i in listA:
    back(i, 0, b-1)

if len(answer) == 0:
    print(0)
else:
    answer.sort()
    print(len(answer))
    print(" ".join(map(str, answer)))
