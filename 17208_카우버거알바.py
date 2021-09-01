import sys
sys.stdin = open('inputs.text')

n, ham, pota = map(int,sys.stdin.readline().split())
matrix = [[[0] * (pota+1) for _ in range(ham+1)] for _ in range(n+1)]


for k in range(1,n+1):
    item = list(map(int,sys.stdin.readline().split()))
    for i in range(1,ham+1):
        for j in range(1,pota+1):
            if i < item[0]:
                matrix[k][i][j] = matrix[k-1][i][j]
            else:
                if j < item[1]:
                    matrix[k][i][j] = matrix[k-1][i][j]
                else:
                    matrix[k][i][j] = max(1+matrix[k-1][i-item[0]][j-item[1]], matrix[k-1][i][j])
print(matrix[-1][-1][-1])