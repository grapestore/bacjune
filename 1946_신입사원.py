import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
for _ in range(n):
    t1 = int(sys.stdin.readline())
    matrix1 = [0]*(t1+1)
    for _ in range(t1):
        a,b = map(int,sys.stdin.readline().split())
        matrix1[a] = b
    min1 = 100001
    count1=0
    for data1 in matrix1[1:]:
        if min1>data1:
            min1 = data1
            count1+=1
    print(count1)