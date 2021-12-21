import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
star = [[' ' for _ in range(n)] for _ in range(n)]

def fill(depth,x,y):
  if depth == 1:
    star[y][x] = '*'
  else:
    next_size = depth//3
    fill(next_size,x+0*next_size,y+0*next_size)
    fill(next_size,x+0*next_size,y+1*next_size)
    fill(next_size,x+0*next_size,y+2*next_size)

    fill(next_size,x+1*next_size,y+0*next_size)
    # fill(next_size,x+1*next_size,y+1*next_size)
    fill(next_size,x+1*next_size,y+2*next_size)

    fill(next_size,x+2*next_size,y+0*next_size)
    fill(next_size,x+2*next_size,y+1*next_size)
    fill(next_size,x+2*next_size,y+2*next_size)


  



fill(n,0,0)
for x in star:
  print(''.join(x))
  # print(*x)