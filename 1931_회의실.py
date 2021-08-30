import sys
sys.stdin = open('inputs.text')

matrix = []
n = int(sys.stdin.readline())
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    dif = b - a
    matrix.append([a,b,dif])

matrix.sort(key=lambda x: (x[1],x[2]))
start,end,diff = matrix.pop(0)
result = []
result.append([start,end,diff])
while matrix:
    start2,end2,diff2 = matrix.pop(0)
    if start2>=end:
        result.append([start2,end2,diff2])
        start=start2
        end=end2
        diff=diff2

print(len(result))