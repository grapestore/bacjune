import sys
from collections import deque

sys.stdin = open('inputs.text')


marble, m = map(int,sys.stdin.readline().split())
graph1 = [[] for _ in range(marble+1)]
graph2 = [[] for _ in range(marble+1)]
count = 0
mid_count = marble//2 + 1
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph1[b].append(a)
    graph2[a].append(b)

def bfs1(start):
    global count
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph1[node])
    if len(visited)>mid_count:
        count += 1
    return visited

def bfs2(start):
    global count
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph2[node])
    if len(visited)>mid_count:
        count += 1
    return visited

for i in range(1,marble+1):
    bfs1(i)
    bfs2(i)
print(count)