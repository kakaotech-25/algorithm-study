import sys

input = sys.stdin.readline


n =int(input())

arr = list(map(int,input().split()))

brr = list(map(int,input().split()))
count=0

for i in range(n):
    if arr[i] == brr[i]:
        continue
    elif arr[i]>brr[i]:
        while(arr[i] != brr[i]):
            arr[i]-=1
            count+=1
            
print(count)
           
    