import sys
from collections import deque

num = int(sys.stdin.readline())
matrix=[[0]*(num+1) for i in range(num+1)]
line_count = int(sys.stdin.readline())
for i in range(line_count):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def bfs(start):
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for i in range(1,num+1):
            if i not in visited and matrix[node][i] == 1:
                queue.append(i)
                visited.append(i)
    return visited

print(len(bfs(1))-1)