import sys
sys.stdin = open('inputs.text')

n, target = map(int,sys.stdin.readline().split())
matrix = [[0] * (target+1) for _ in range(n+1)]
result = dict()

for i in range(1,n+1):
    item = list(map(int,sys.stdin.readline().split()))
    for j in range(1,target+1):
        if j < item[0]:
            matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])
        else:
            matrix[i][j] = max(item[1]+matrix[i-1][j-item[0]], matrix[i-1][j])
print(matrix[-1][-1])