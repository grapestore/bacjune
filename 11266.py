import sys
sys.stdin = open('inputs.text')
sys.setrecursionlimit(10000)
vertex, edge = map(int,sys.stdin.readline().split())
real_graph = [[] for _ in range(vertex+1)]


for _ in range(edge):
    a,b = map(int,sys.stdin.readline().split())
    real_graph[a].append(b)
    real_graph[b].append(a)

def init_dfs(start):
    for node in real_graph[start]:
        if visit[node] == 0:
            visit[node] = 1
            init_dfs(node)

def dfs(start):
    for node in real_graph[start]:
        if visit[node] == 0:
            visit[node] = 1
            dfs(node)

visit = [0] * (vertex+1)           
max_size = 0
result=[]
init_dfs(1)
lens = visit.count(1)
#lens = 7
for i in range(1,vertex+1):
    visit = [0] * (vertex+1)
    visit[i] = 1
    if visit[i] == 0:
        dfs(1)
        answer = visit.count(1)
        if lens - answer>1:
            result.append(i)
    else:
        dfs(2)
        answer = visit.count(1)
        if lens - answer>1:
            result.append(i)

print(len(result))
print(*result)