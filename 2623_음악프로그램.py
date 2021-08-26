import sys
from collections import deque
sys.stdin = open('inputs.text')

n, pd = map(int,sys.stdin.readline().split())
in_degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
ans = []
for _ in range(pd):
    temp = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(temp)):
        in_degree[temp[i]] = in_degree[temp[i]] + len(temp[1:i])
        graph[temp[i]] = graph[temp[i]] + temp[i+1:]

queue = deque()
for i in range(1,n+1):
    if in_degree[i] == 0:
        queue.append(i)
        
while queue:
    node = queue.popleft()
    ans.append(node)
    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
for check in in_degree:
    if check > 0:
        print(0)
        exit()
for answer in ans:
    print(answer)