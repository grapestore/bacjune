import sys
sys.stdin = open('inputs.text')

n, target = map(int,sys.stdin.readline().split())
matrix = []
for _ in range(n):
    matrix.append(int(sys.stdin.readline()))
matrix.sort(reverse=True)

i = 0
count = 0
while target!=0:
    if matrix[i]<=target:
        target -= matrix[i]
        count += 1
    else:
        i += 1
print(count)