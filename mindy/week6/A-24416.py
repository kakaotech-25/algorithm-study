import sys

input = sys.stdin.readline

n = int(input())
x,y=0,0

def fib(n):
    global x
    if n ==1 or n==2:
        x +=1
        return 1
    else: return (fib(n-1)+fib(n-2))
    
f =[0] * n
def fibonacci(n):
    global y
    f[0] =1
    f[1] =1
    for i in range(2,n):
        y +=1
        f[i] = f[i-1]+f[i-2]
    return f[n-1]


fib(n)
fibonacci(n)

print(x,y)