import sys

n = 3
jump = 10

matrix = [[0] * n for _ in range(n)]
possible = [[False] * n for _ in range(n)]
x = 0
y = 0
matrix[0][0] = 1
cnt = 2
save_return = [-111,-111]
# 0 right / 1 down / 2 left / 3 up #
direction = 0
target = n*n
while (True):
  count = 0
  total_count = 0
  while count < jump:
    possible[y][x] = True

    # direction check #
    if direction== 0 and (x == n-1 or possible[y][x+1] == True):
      direction = 1
    elif direction==1 and (y == n-1 or possible[y+1][x] == True):
      direction = 2
    elif direction==2 and (x == 0 or possible[y][x-1] == True):
      direction = 3
    elif direction==3 and (y == 0 or possible[y-1][x] == True):
      direction = 0

    if direction == 0:
      x += 1
    elif direction == 1:
      y += 1
    elif direction == 2:
      x -= 1
    elif direction == 3:
      y -= 1
    

    # pass check #
    if matrix[y][x] == 0:
      count += 1
      
    if [y,x] == save_return:
      y = 0
      x = 0
      possible = [[False] * n for _ in range(n)]

  if matrix[y][x] == 0:
    matrix[y][x] = cnt
    if cnt == target:
      print([y+1,x+1])
      exit()
    cnt += 1
  try:
    if possible[y-1][x] == True and possible[y+1][x] == True and possible[y][x-1] == True and possible[y][x+1] == True:
      save_return = [y,x]
      y = 0
      x = 0
      possible = [[False] * n for _ in range(n)]
  except:
    continue






