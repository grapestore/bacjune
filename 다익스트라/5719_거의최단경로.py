import heapq
import sys
from collections import defaultdict, deque
sys.stdin = open('inputs.text')
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def djikstra(start):
  
  distance[start] = 0
  queue = []
  heapq.heappush(queue,[0,start])
  while queue:
    dis, now_node = heapq.heappop(queue)
    if distance[now_node] < dis:
      continue
    for next_node in graph[now_node]:
      cost = dis + graph[now_node][next_node]
      if distance[next_node] > cost:
        distance[next_node] = cost
        heapq.heappush(queue,[cost,next_node])
  return

def bfs(end):

  queue = deque([end])
  remove_list = []
  while queue:
    reverse = queue.popleft()
    if start == reverse:
      continue
    for prev, cost in graph_r[reverse]:
      if distance[prev] + graph[prev][reverse] == distance[reverse]:
        if [prev, reverse] not in remove_list:
          remove_list.append([prev, reverse])
          queue.append(prev)

      
  return remove_list


while True:

  vertex_num, e = map(int,sys.stdin.readline().split())
  if vertex_num==0 and e==0:
    break

  start, end = map(int,sys.stdin.readline().split())

  graph = [dict() for _ in range(vertex_num+1)]
  graph_r = [[] for _ in range(vertex_num+1)]
  
  for _ in range(e):
    u,v,p = map(int,sys.stdin.readline().split())
    graph[u][v] = p
    graph_r[v].append([u,p])

  distance = [INF]*(vertex_num)
  djikstra(start)

  for prev, next in bfs(end):
    del graph[prev][next]

  distance = [INF]*(vertex_num)
  djikstra(start)
  if distance[end] == INF:
    print(-1)
  else:
    print(distance[end])
