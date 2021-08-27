import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
memo = dict()
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
a = arr[0]
b = arr[1]
c = arr[2]
memo[3] = min(a[0]*b[0]*b[1] + a[0]*b[1]*c[1], 
print(memo)