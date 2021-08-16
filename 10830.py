import sys


def multiplication(a,n):
    if n < 2:
        return a
    else:
        half=multiplication(a,n//2)
        if n%2==0:
            return calc(half,half)
        else:
            return calc(calc(half,half),a)

def nomultiplication(a,n):
    c = [[0] * value for i in range(value)]
    for i in range(value):
        for j in range(value):
            c[i][j] = a[i][j] % 1000
    return c

def calc(a,b):
    c = [[0] * value for i in range(value)]
    for i in range(value):
        for j in range(value):
            for k in range(value):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % 1000
    return c


value, num = map(int,sys.stdin.readline().split())
arr = []
for i in range(value):
    temp = list(map(int,sys.stdin.readline().split()))
    arr.append(temp)
if num > 1:
    for x in multiplication(arr,num):
        print(' '.join(map(str, x)))
else:
    for y in nomultiplication(arr,num):
        print(' '.join(map(str, y)))
