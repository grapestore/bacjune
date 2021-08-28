import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
memo = [[0]*n for _ in range(n)]


arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(1, n): 
    for j in range(n-i): 
        memo[j][j+i] = float('inf')
        for k in range(j, j+i): 
            memo[j][j+i] = min(memo[j][j+i], memo[j][k] + memo[k+1][j+i] + arr[j][0]*arr[k][1]*arr[j+i][1])


print(memo[0][n-1])