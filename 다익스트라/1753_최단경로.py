import sys
import heapq
sys.stdin = open('inputs.text')
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

vertex_num,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(vertex_num+1)]
trace_arr = [[] for _ in range(vertex_num+1)]
for i in range(vertex_num+1):
  trace_arr[i].append(i)
for _ in range(e):
  u,v,w = map(int,sys.stdin.readline().split())
  graph[u].append([v,w])

def djikstra(start,w):

  distance = [INF] * (vertex_num+1)
  distance[start] = 0
  queue = []
  heapq.heappush(queue,[w,start])

  while queue:
    cost, now_node = heapq.heappop(queue)
    if distance[now_node] < cost:
      continue
    for next_node,cst in graph[now_node]:
      spanning = cost + cst
      if distance[next_node] > spanning:
        distance[next_node] = spanning
        trace_arr[next_node] = trace_arr[now_node] + [next_node]
        heapq.heappush(queue,[spanning,next_node])
  print(trace_arr)
  for x in distance[1:]:
    if x == INF:
      print('INF')
    else:
      print(x)
  return

djikstra(start,0)