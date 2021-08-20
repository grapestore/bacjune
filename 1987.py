import sys


r, c = map(int,sys.stdin.readline().split())
matrix = []
for i in range(r):
    arr=[]
    temp = sys.stdin.readline().rstrip()
    for j in temp:
        arr.append(j)
    matrix.append(arr)


def dfs(start,visited2=[]):
    global maximum
    visited2.append(matrix[start[0]][start[1]])
    if len(visited2) > maximum:
        maximum = len(visited2)
    for node in graph[start[0],start[1]]:
        if matrix[node[0]][node[1]] not in visited2:
            dfs(node,visited2)
            visited2.pop()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
x,y = 0,0
count = 0
graph = dict()
for i in range(r):
    for j in range(c):
        temp = []
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]
            if nx<0 or nx>=c or ny<0 or ny >= r:
                continue
            else:
                temp.append([ny,nx])
        graph[i,j] = temp
maximum = 0
dfs([0,0])
print(maximum)