import sys
sys.setrecursionlimit(10**6)

def multiplication(a,n):
    if n == 1:
        return a % c
    remain = multiplication(a,n//2)
    if n % 2 == 0:
        return remain * remain % c
    else:
        return remain * remain * a % c


value, num, c = map(int,sys.stdin.readline().split())

print(multiplication(value,num)
