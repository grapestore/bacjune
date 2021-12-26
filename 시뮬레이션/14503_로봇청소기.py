import sys
from collections import deque
sys.stdin = open('inputs.text')


def game(direction):
  dx=[0,1,0,-1]
  dy=[-1,0,1,0]
  y = r
  x = c
  queue = deque([[x,y]])
  count = 1
  direc = direction
  while queue:
    x,y = queue.popleft()
    matrix[y][x] = 2
    for _ in range(4):
      direc = (direc-1)%4
      nx = x + dx[direc]
      ny = y + dy[direc]
      if 0<nx<m-1 and 0<ny<n-1 and matrix[ny][nx] == 0:
        count += 1
        queue.append([nx,ny])
        break
    else:
      back = (direc-2)%4
      nx = x + dx[back]
      ny = y + dy[back]
      if 0<nx<m-1 and 0<ny<n-1 and matrix[ny][nx] != 1:
        queue.append([nx,ny])
      elif 0<nx<m-1 and 0<ny<n-1 and matrix[ny][nx] == 1:
        return count
  return count
        


n, m = map(int,sys.stdin.readline().split())
r, c, direction = map(int,sys.stdin.readline().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(int,sys.stdin.readline().split())))

print(game(direction))