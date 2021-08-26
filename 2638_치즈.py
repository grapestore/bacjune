import sys
from collections import deque
sys.stdin = open('inputs.text')

n,m = map(int,sys.stdin.readline().split())
matrix = []
visit = [[0]*m for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

cheese = 0
for j in range(n):
    for i in range(m):
        if matrix[j][i] > 0:
            cheese += 1

def bfs(start):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visit[start[0]][start[1]] = 1
    matrix[start[0]][start[1]] = -1
    queue = deque([start])

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=m or ny>=n or visit[ny][nx] == 1:
                continue
            elif matrix[ny][nx] == 0 or matrix[ny][nx] == -1:
                matrix[ny][nx] = -1
                visit[ny][nx] = 1
                queue.append([ny,nx])
            elif matrix[ny][nx] > 0:
                matrix[ny][nx] += 1


day = 0
while cheese > 0:
    cheese = 0
    bfs([0,0])
    for j in range(n):
        for i in range(m):
            visit[j][i] = 0
            if matrix[j][i] >= 3:
                matrix[j][i] = -1
            elif 0<matrix[j][i] <3:
                matrix[j][i] = 1
                cheese += 1
    day+=1
    if cheese == 0:
        break

print(day)