from collections import deque

def check(matrix , j, i):
    visit = [[False] * 5 for _ in range(5)]
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    queue = deque([[j,i,0]])
    while queue:
        y,x,dis = queue.popleft()
        visit[y][x] = True
        for u in range(4):
            nx = x + dx[u]
            ny = y + dy[u]
            if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == False:
                if matrix[ny][nx] == 'P':
                    return 0
                elif matrix[ny][nx] == 'O' and dis<1:
                    visit[ny][nx] = True
                    queue.append([ny,nx,dis+1])
    return 1

def solution(places):
    answer = []
    for x in places:
        matrix = []
        result = 1
        for y in x:
            matrix.append(list(map(str,y)))
            
        for j in range(5):
            normal = True
            for i in range(5):
                if matrix[j][i] == 'P':
                    result = check(matrix, j, i)
                    if result == 0:
                        normal = False
                        break
            if normal == False:
                break
        answer.append(result)
        
    return answer