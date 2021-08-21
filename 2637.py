import sys
from collections import deque
sys.stdin = open('inputs.text')

num = int(input())
index = int(input())
in_degree = [0] * (num+1)
graph = [[] for i in range(num+1)]
needs = [[0] * (num + 1) for _ in range(num + 1)]
mini_part = []
for _ in range(index):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[b].append((a,c))
    in_degree[a] += 1

queue = deque()
for idx in range(1,num):
    if in_degree[idx] == 0:
        mini_part.append(idx)
        queue.append(idx)

while queue:
    now = queue.popleft()
    for next, next_cost in graph[now]:
        if now in mini_part:
            needs[next][now] = next_cost
        else:
            for i in range(1,num+1):
                needs[next][i] += needs[now][i] * next_cost

    for j in graph[now]:
        in_degree[j[0]] -= 1
        if in_degree[j[0]] == 0:
            queue.append(j[0])

for idx in range(1,num+1):
    if needs[num][idx] != 0:
        print(f'{idx} {needs[num][idx]}')