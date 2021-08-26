import sys
from collections import deque
sys.stdin = open('inputs.text')


n = int(sys.stdin.readline())
matrix = []
count = 0
time = 0
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 9:
            shark_loca = [j,i,0]
            matrix[j][i] = 0
        elif matrix[j][i] < 9 and matrix[j][i] > 0:
            count += 1


def bfs(start):
    global count, init_size

    visit = [start]
    ans = []
    
    queue = deque([start])

    while queue:
        y,x,day = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            elif matrix[ny][nx] > init_size:
                continue
            elif (matrix[ny][nx] == init_size or matrix[ny][nx] == 0) and [ny,nx] not in visit:
                queue.append([ny,nx,day+1])
                visit.append([ny,nx])
                continue
            elif matrix[ny][nx]>0 and matrix[ny][nx]<init_size and [ny,nx] not in visit:
                ans.append([ny,nx,day+1])
                visit.append([ny,nx])
    if len(ans) == 0:
        return
    else:
        return ans

if count == 0:
    print(0)
    exit()
else:
    init_size = 2
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    eat_count = 0
    while True:
        answer = bfs(shark_loca)
        if answer == None:
            print(time)
            break
        answer = deque(sorted(answer, key=lambda x: (x[2],x[0],x[1])))
        min_dis = answer.popleft()
        matrix[min_dis[0]][min_dis[1]] = 0
        time = min_dis[2]
        shark_loca = [min_dis[0],min_dis[1],min_dis[2]]
        eat_count += 1
        if eat_count == init_size:
            init_size += 1
            eat_count = 0
