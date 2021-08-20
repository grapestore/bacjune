import sys
from collections import deque



m,n,h = map(int,sys.stdin.readline().split())
matrix = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,sys.stdin.readline().split())))
    matrix.append(temp)
stable = False
count = 0
check_count = 0
zero_count = 0
one_lo = []
maximum = 0
for q in range(h):
    for w in range(n):
        for e in range(m):
            if matrix[q][w][e] == 1:
                one_lo.append([q,w,e])
            if matrix[q][w][e] >= 0:
                count += 1
            if matrix[q][w][e] == 0:
                zero_count += 1


def bfs(one_lo):
    global maximum,check_count
    queue = deque()
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    for asd in one_lo:
        queue.append(asd)
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
                continue
            if matrix[nz][ny][nx] == -1:
                continue
            elif matrix[nz][ny][nx] > 0:
                continue
            elif matrix[nz][ny][nx] == 0:
                check_count += 1
                queue.append((nz,ny,nx))
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                if matrix[z][y][x] + 1 > maximum:
                    maximum = matrix[z][y][x] + 1


if zero_count == 0 and count>0:
    stable = True
    print(0)
elif stable == False:            
    bfs(one_lo)
    if check_count == zero_count and count>0:
        print(maximum-1)
    else:
        print(-1)




