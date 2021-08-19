import sys
from collections import deque

num = int(sys.stdin.readline())
matrix=[[0]*(num+1) for i in range(num+1)]
line_count = int(sys.stdin.readline())
for i in range(line_count):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(start, visited=[]):
    visited.append(start)

    for i in range(1,num+1):
        if i not in visited and matrix[start][i] == 1:
            dfs(i,visited)

    return visited




print(len(dfs(1))-1)