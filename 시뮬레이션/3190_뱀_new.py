import sys
from collections import deque
sys.stdin = open('inputs.text')

def change(d,c):
  if c == 'D':
    d = (d+1)%4
  else:
    d = (d-1)%4
  return d

def game():
  
  dx = [0,1,0,-1]
  dy = [-1,0,1,0]
  x,y = 0,0
  direction = 1
  time = 1
  visit = deque([[x,y]])
  while True:
    x = x + dx[direction]
    y = y + dy[direction]
    if 0<=x<n and 0<=y<n and matrix[y][x] != 2:
      if matrix[y][x] == 0:
        pre_x, pre_y = visit.popleft()
        matrix[pre_y][pre_x] = 0 

      matrix[y][x] = 2
      visit.append([x,y])
      if time in command.keys():
        direction = change(direction,command[time])
      time += 1
    else:
      return time


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
matrix = [[0] * n for _ in range(n)]

for _ in range(k):
  j,i = map(int,sys.stdin.readline().split())
  matrix[j-1][i-1] = 1

command_num = int(sys.stdin.readline())
command = dict()
for _ in range(command_num):
  time, direc = sys.stdin.readline().split()
  command[int(time)] = direc
print(game())

