from collections import deque

def change(direction):
  return direction%4
    
def game(x1,y1,x2,y2):
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]
  direction = 0
  temp = matrix[x1][y1]
  visit = [temp]
  queue = deque([temp])
  y,x = x1,y1
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if y1<=nx<y2 and x1<=ny<x2:
      if matrix[ny][nx] == temp:
        matrix[ny][nx] = queue.popleft()
        break
      visit.append(matrix[ny][nx])
      queue.append(matrix[ny][nx])
      matrix[ny][nx] = queue.popleft()
      x,y = nx,ny
    else:
      direction = change(direction+1)
  
    
  answer.append(min(visit))
  return


rows= 6
columns=6
queries=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

answer = []
matrix = [[0] * columns for _ in range(rows)]
count = 1
for j in range(rows):
  for i in range(columns):
    matrix[j][i] = count
    count+=1
        
for x1,y1,x2,y2 in queries:
  game(x1-1,y1-1,x2,y2)
print(answer)