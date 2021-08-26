import sys 
sys.setrecursionlimit(10000) 

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 

def dfs(x, y, h): 
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        if(0 <= nx < N) and (0 <= ny < N): 
            if arr[nx][ny] > h and done[nx][ny] == 0: 
                done[nx][ny] = 1 
                dfs(nx, ny, h) 

N = int(sys.stdin.readline())
arr = []

for insert_arr in range(N):
    temp_arr = []
    for temp in map(int, sys.stdin.readline().split()):
        temp_arr.append(temp)
    arr.append(temp_arr)

ans = 0 

### increase water ###
for k in range(max(map(max, arr))): 
    cnt = 0 
    done = [[0]*N for _ in range(N)]
    for i in range(N): 
        for j in range(N): 
            if arr[i][j] > k and done[i][j] == 0: 
                done[i][j] = 1 
                cnt += 1 
                dfs(i, j, k) 
                ans = max(ans, cnt) 
print(ans)
