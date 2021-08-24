import sys
sys.stdin = open('inputs.text')
sys.setrecursionlimit(10000)

m,n,c = map(int,sys.stdin.readline().split())
matrix = [[0]*n for _ in range(m)]
visit = [[0]*n for _ in range(m)]
zero_loca = []
for _ in range(c):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for j in range(y1,y2):
        for i in range(x1,x2):
            matrix[j][i] = 1
for j in range(m):
    for i in range(n):
        if matrix[j][i] == 0:
            zero_loca.append([j,i])

def dfs(y,x):
    global maximum, count

    count += 1
    if count > maximum:
        maximum = count
    visit[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or nx<0 or ny>=m or nx>=n:
            continue
        if matrix[ny][nx] > 0 or visit[ny][nx]>0:
            continue
        
        maximum = dfs(ny,nx)

    return maximum

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []            
for y,x in zero_loca:
    maximum = 1
    count = 0
    if visit[y][x] == 0:
        answer.append(dfs(y,x))
answer = sorted(answer)
print(len(answer))
print(*answer)
