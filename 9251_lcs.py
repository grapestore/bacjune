import sys
sys.stdin = open('inputs.text')

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
matrix = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])

print(matrix[-1][-1])
