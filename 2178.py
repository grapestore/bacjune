import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())
matrix = []
for i in range(n):
    temp = list((map(int,input())))
    matrix.append(temp)
count = 0
def bfs(x,y):
    global count
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))

    return matrix[n-1][m-1]


print(bfs(0,0))