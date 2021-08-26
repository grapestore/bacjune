import sys


num1 = int(sys.stdin.readline())
A=[]
for repeat1 in map(int,sys.stdin.readline().split()):
    A.append(repeat1)
A = set(A)
num2 = int(sys.stdin.readline())
for target in map(int,sys.stdin.readline().split()):
    if target in A:
        print(1)
    else:
        print(0)