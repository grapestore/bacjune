import sys 
sys.stdin = open('inputs.text')
sys.setrecursionlimit(10000)

y,x = map(int,sys.stdin.readline().split())
matrix = []
visit_check = [[0] * x for _ in range(y)]
for _ in range(y):
    matrix.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(start_y,start_x):
    for k in range(4):
        next_y = start_y + dy[k]
        next_x = start_x + dx[k]
        if next_y<0 or next_x<0 or next_y>=y or next_x>=x:
            continue
        if matrix[next_y][next_x] > 0 and visit_check[next_y][next_x] == 0:
            visit_check[next_y][next_x] = 1
            dfs(next_y, next_x)


maximum = 0
count = 0
while True:
    mount_count = 0
    ice_loca = []
    ice_count = 0
    visit_check = [[0] * x for _ in range(y)]
    
    ## 빙하 위치 체크 및 탐색
    for j in range(y):
        for i in range(x):
            if matrix[j][i] > 0:
                ice_count+=1
                #ice_loca.append([j,i])
                if visit_check[j][i]==0:
                    visit_check[j][i] = 1
                    dfs(j, i)
                    mount_count += 1
    
    if ice_count < 1:
        break
    ## 빙하 크기 내리기
    for j in range(y):
        for i in range(x):
            if matrix[j][i] > 0:
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]
                    if ny<0 or nx<0 or ny>=y or nx>=x or [ny,nx] in ice_loca:
                        continue
                    if matrix[ny][nx] < 1 and visit_check[ny][nx] == 0:
                        matrix[j][i] -= 1
    
    
    count += 1
    ## 빙하 2조각이면 끝
    if mount_count>1:
        print(count-1)
        exit()
    
print(0)