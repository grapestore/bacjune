import sys

def dfs(y,x,size):
    visit[y][x] = True
    result = size
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<width and 0<=ny<height and visit[ny][nx] == False and matrix[ny][nx] == 1:
            result += dfs(ny,nx,1)

    return result

def solution(v):
    sys.setrecursionlimit(3000)
    global visit, width, height, matrix
    matrix = v
    width = len(v[0])
    height = len(v)
    visit = [[False]*width for _ in range(height)]
    cnt = 0
    answer = []
    for j in range(height):
        for i in range(width):
            if visit[j][i] == False and matrix[j][i] == 1:
                cnt += 1
                answer.append(dfs(j,i,1))

    if answer:
        return [len(answer), max(answer)]
    else:
        return [0,0]