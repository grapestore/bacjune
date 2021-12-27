

R = [[3,9,2,7],[10,6,8,4],[1,4,9,10],[5,7,8,4]]

n = len(R)
m = len(R[0])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = [[1] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
def dfs(y,x):
  for idx in range(4):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0<nx<m and 0<ny<n:
      if R[y][x] < R[ny][nx] and visit[ny][nx] == False and result[y][x]+1>result[ny][nx]:
        visit[ny][nx] = True
        result[ny][nx] = result[y][x] + 1
        dfs(ny,nx)
        visit[ny][nx] = False

for j in range(n):
  for i in range(m):
    visit[j][i] = True
    dfs(j,i)
    visit[j][i] = False

max_length = 0
for i in result:
  length = max(i)
  if max_length<length:
    max_length = length
print(max_length)

import sys
sys.setrecursionlimit(10**6)

def solution(R):
    n = len(R)
    m = len(R[0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    result = [[1] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    def dfs(y,x):
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<m and 0<=ny<n:
                if R[y][x] < R[ny][nx] and visit[ny][nx] == False and result[y][x]+1>result[ny][nx]:
                    visit[ny][nx] = True
                    result[ny][nx] = result[y][x] + 1
                    dfs(ny,nx)
                    visit[ny][nx] = False
        return

    for j in range(n):
        for i in range(m):
            visit[j][i] = True
            dfs(j,i)
            visit[j][i] = False

    max_length = 0
    for i in result:
        length = max(i)
        if max_length<length:
            max_length = length
    return max_length