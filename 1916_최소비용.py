import sys
import heapq
sys.stdin = open('inputs.text')
INF = int(1e9)

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())

W = [[] for _ in range(n+1)]

for _ in range(e):
    v1,v2,value = map(int,sys.stdin.readline().split())
    W[v1].append((v2,value))

start, end = map(int,sys.stdin.readline().split())

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in W[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
distance = [INF] * (n+1)
dij(start)

print(distance[end])