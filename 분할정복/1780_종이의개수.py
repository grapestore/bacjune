import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
  arr.append(list(map(int,sys.stdin.readline().split())))
minus = 0
zero = 0
plus = 0

def divide(depth,x,y):
  global minus, zero, plus
  if depth == 1:
    check = arr[y][x]
    if check == 0:
      zero += 1
    elif check == 1:
      plus += 1
    else:
      minus += 1
    return
  count_minus, count_plus, count_zero = [0,0,0]
  for j in range(y,y+depth):
    game = True
    for i in range(x,x+depth):
      if arr[j][i] == -1:
        count_minus += 1
      elif arr[j][i] == 0:
        count_zero += 1
      elif arr[j][i] == 1:
        count_plus += 1
      if (count_minus>0 and count_plus>0) or (count_zero>0 and count_plus>0) or(count_minus>0 and count_zero>0):
        game = False
        break
    if game == False:
      break
  
  if count_zero==0 and count_plus==0:
    minus += 1
    return
  elif count_zero==0 and count_minus==0:
    plus += 1
    return
  elif count_plus==0 and count_minus==0:
    zero += 1
    return

  next_size = depth//3
  divide(next_size, x+0*next_size, y+0*next_size)
  divide(next_size, x+0*next_size, y+1*next_size)
  divide(next_size, x+0*next_size, y+2*next_size)

  divide(next_size, x+1*next_size, y+0*next_size)
  divide(next_size, x+1*next_size, y+1*next_size)
  divide(next_size, x+1*next_size, y+2*next_size)

  divide(next_size, x+2*next_size, y+0*next_size)
  divide(next_size, x+2*next_size, y+1*next_size)
  divide(next_size, x+2*next_size, y+2*next_size)

divide(n,0,0)
print(minus, zero, plus)