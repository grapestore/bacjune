from collections import deque
import sys

v,e = map(int, sys.stdin.readline().split())
in_dgree = [0] * (v+1)
graph = [[] for i in range(v+1)]
result = []
for i in range(e):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    in_dgree[b] += 1

def topology_sort():
    queue = deque()

    for i in range(1,v+1):
        if in_dgree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        result.append(node)
        for i in graph[node]:
            in_dgree[i] -= 1
            if in_dgree[i] == 0:
                queue.append(i)

topology_sort()
print(' '.join(map(str,result)))
