from collections import defaultdict, deque
def dikjstra(n,start):

    distance = [999999]*(n+1)
    distance[start] = 0
    queue = deque([[start,0]])
    while queue:
        cur, cst = queue.popleft()
        for next, cost in W[cur]:
            if cst+cost < distance[next]:
                distance[next] = cst+cost
                queue.append([next, cst+cost])
    
    return distance

def solution(n, edge):
    global W
    W = defaultdict(list)
    for x in edge:
        W[x[0]].append([x[1],1])
        W[x[1]].append([x[0],1])

    result = dikjstra(n,1)
    temp = sorted(set(result))
    answer = result.count(temp[-2])
    return answer