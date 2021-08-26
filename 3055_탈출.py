import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
matrix = []
S_loca = []
water_loca = []
queue = deque()
for x in range(r):
    temp = []
    count = 0
    for y in sys.stdin.readline().rstrip():
        temp.append(y)
        if y == 'S':
            S_loca.append([x,count,'S'])
        elif y == '*':
            water_loca.append([x,count,'W'])
        count += 1
    matrix.append(temp)
matrix[S_loca[0][0]][S_loca[0][1]] = 1

def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        y,x,check = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=c or ny>=r:
                continue
            if matrix[ny][nx] == '.':
                if check == 'S':
                    matrix[ny][nx] = matrix[y][x] + 1
                    queue.append([ny,nx,'S'])
                elif check == 'W':
                    matrix[ny][nx] = '*'
                    queue.append([ny,nx,'W'])
            elif matrix[ny][nx] == '*':
                continue
            elif matrix[ny][nx] == 'X':
                continue
            elif matrix[ny][nx] == 'D' and check == 'S':
                matrix[ny][nx] = matrix[y][x] + 1
                return matrix[ny][nx] -1
    return 'KAKTUS'
for asd in water_loca:
    queue.append(asd)
for asd in S_loca:
    queue.append(asd)


print(bfs())


