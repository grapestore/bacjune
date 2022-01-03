def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer


# from collections import deque

# def change(direction):
#   return direction%4
    
# def game(x1,y1,x2,y2):
#   dx = [1,0,-1,0]
#   dy = [0,1,0,-1]
#   direction = 0
#   temp = matrix[x1][y1]
#   visit = [temp]
#   queue = deque([temp])
#   y,x = x1,y1
#   while True:
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if y1<=nx<y2 and x1<=ny<x2:
#       if matrix[ny][nx] == temp:
#         matrix[ny][nx] = queue.popleft()
#         break
#       visit.append(matrix[ny][nx])
#       queue.append(matrix[ny][nx])
#       matrix[ny][nx] = queue.popleft()
#       x,y = nx,ny
#     else:
#       direction = change(direction+1)
  
    
#   answer.append(min(visit))
#   return


# rows= 6
# columns=6
# queries=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# answer = []
# matrix = [[0] * columns for _ in range(rows)]
# count = 1
# for j in range(rows):
#   for i in range(columns):
#     matrix[j][i] = count
#     count+=1
        
# for x1,y1,x2,y2 in queries:
#   game(x1-1,y1-1,x2,y2)
# print(answer)