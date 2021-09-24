import sys
sys.stdin = open('inputs.text')


num = int(sys.stdin.readline())

matrix = []
for _ in range(num):
  matrix.append(list(map(int,sys.stdin.readline().split())))
inf = 99999999
mini = 99999999

for i in range(3):
  dp = [[0] * 3 for _ in range(num)]
  dp[0][i] = matrix[0][i]
  dp[0][i-1] = inf
  dp[0][(i+1)%3] = inf

  for x in range(1,num):
    for j in range(3):
      if x == num-1:
        dp[x][j] = min(dp[x-1][j-1]+matrix[x][j],
                  dp[x-1][(j+1)%3]+matrix[x][j])
        if dp[0][j] != inf:
          dp[x][j] = inf
        continue

      dp[x][j] = min(dp[x-1][j-1]+matrix[x][j],
                  dp[x-1][(j+1)%3]+matrix[x][j])
  if min(dp[-1]) < mini:
    mini = min(dp[-1])

print(mini)