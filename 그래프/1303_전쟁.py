from os import truncate
import sys
from collections import deque

sys.stdin = open('inputs.text')

n, m = map(int, sys.stdin.readline().split())
arr = []
visit = []
W = []
B = []

for _ in range(m):
  arr.append(list(sys.stdin.readline().rstrip()))
  visit.append([False for _ in range(n)])

dx = [1,-1,0,0]
dy = [0,0,1,-1]  

def dfs(x,y,depth):
  count = depth
  visit[y][x] = True
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if 0<=nx<n and 0<=ny<m:
      if arr[ny][nx] == arr[y][x] and visit[ny][nx] == False:
        count = dfs(nx,ny,count+1)
  if depth == 1:
    if arr[y][x] == 'W':
      W.append(count*count)
    else:
      B.append(count*count)

  return count

for j in range(m):
  for i in range(n):
    if visit[j][i] == False:
      dfs(i,j,1)
print(sum(W),sum(B))