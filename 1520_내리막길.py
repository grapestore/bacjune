import sys
#sys.stdin = open('inputs.text')

n,m = map(int,sys.stdin.readline().split())

matrix = []
for _ in range(n):
  matrix.append(list(map(int,sys.stdin.readline().split())))

dp = [[-1]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dp[-1][-1] = 1

def dfs(y,x):
  if dp[y][x] != -1:
    return dp[y][x]
  dp[y][x] = 0
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0<=nx<m and 0<=ny<n and matrix[ny][nx]<matrix[y][x]:
      dp[y][x] += dfs(ny,nx)

  return dp[y][x]


dfs(0,0)
print(dp[0][0])