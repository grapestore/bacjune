from collections import deque

N,M,start=map(int,input().split())
arr=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b]=arr[b][a]=1
city = []
for x in range(N):
    city.append(x+1)

def dfs(start, visited=[]):
    visited.append(start)
    for i in range(1,N+1):
        if(i not in visited and arr[start][i]==1):
            dfs(i, visited)
    return visited

def bfs(start, visited=[]):
    queue = deque([start])
    visited.append(start)
    while queue:
        node = queue.popleft()
        for i in range(1, N+1):
            if i not in visited and arr[node][i]==1:
                queue.append(i)
                visited.append(i)
    return visited


print(' '.join(map(str,(dfs(start)))))
print(' '.join(map(str,(bfs(start)))))