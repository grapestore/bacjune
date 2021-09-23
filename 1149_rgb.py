import sys
sys.stdin = open('inputs.text')




num = int(sys.stdin.readline())

matrix = []
for _ in range(num):
  matrix.append(list(map(int,sys.stdin.readline().split())))
inf = 99999999
mini = 99999999
# 0 레드 1 초록 2 파랑
for i in range(3):
  dp = [[0] * 3 for _ in range(num)]
  dp[0][i] = matrix[0][i]
  dp[0][i-1] = inf
  dp[0][(i+1)%3] = inf

  for j in range(1,num):
    for k in range(3):
      left = k-1
      right = (k+1)%3
      dp[j][k] = min(dp[j-1][left]+matrix[j][k], dp[j-1][right]+matrix[j][k])
  if min(dp[-1]) < mini:
    mini = min(dp[-1])
    
print(mini)
