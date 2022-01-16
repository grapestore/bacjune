from collections import deque

def game(maps):
    n = len(maps)
    m = len(maps[0])
    
    cost = [[10000 for _ in range(m)] for _ in range(n)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    
    queue = deque([[0,0]])
    cost[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        maps[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if cost[y][x]+1 < cost[ny][nx]:
                    cost[ny][nx] = cost[y][x]+1
                    queue.append([nx,ny])
    
    return cost

def solution(maps):
    answer = 0
    result = game(maps)
    answer = result[-1][-1]
    if answer == 10000:
        return -1
    return answer