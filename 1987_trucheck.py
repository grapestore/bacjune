import sys

def aToIdx(a):
    return ord(a)-ord('A')


r, c = map(int,sys.stdin.readline().split())
matrix = []
g = [[] for _ in range(r)]
visited = [[False] * r for N in range(c)]
for i in range(r):
    g[i] = [aToIdx(x) for x in sys.stdin.readline().rstrip()]


def dfs(start,depth):
    global maximum
    if maximum == 26:
        return
    maximum = max(maximum,depth)
    for node in graph[start[0],start[1]]:
        v = g[node[0]][node[1]]
        if not visited[node[0]][node[1]] and not alpha[v]:
            alpha[v] = True
            visited[node[0]][node[1]] = True
            dfs(node,depth+1)
            visited[node[0]][node[1]] = False
            alpha[v] = False


dx = [1,-1,0,0]
dy = [0,0,1,-1]
x,y = 0,0
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
alpha = [False]*26
alpha[g[0][0]] = True
visited[0][0] = True
dfs([0,0],1)
print(maximum)