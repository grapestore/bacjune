from collections import defaultdict
import heapq

def dikstra(n,info):
    INF = float('inf')
    distance = [INF]*(n+1)
    distance[1] = -1
    queue = [[0,1]]
    while queue:
        cost, cur = heapq.heappop(queue)
        for W, des in info[cur]:
            if distance[des] > W+cost:
                distance[des] = W+cost
                heapq.heappush(queue,[W+cost,des])
    
    return distance

def solution(N, road, K):
    answer = 0
    info = defaultdict(list)
    for a,b,cst in road:
        info[a].append([cst,b])
        info[b].append([cst,a])
        
    for find in dikstra(N,info):
        if find<=K:
            answer+=1

    return answer