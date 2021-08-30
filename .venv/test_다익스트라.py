inf = 999
w = [
    [-1,-1,-1,-1,-1,-1],
    [-1,0,7,4,6,1],
    [-1,inf,0,inf,inf,inf],
    [-1,inf,2,0,5,inf],
    [-1,inf,3,inf,0,inf],
    [-1,inf,inf,inf,1,0]
]

def dijkstra(w):
    n = len(w)-1
    F = []
    touch = [-1] * (n+1)
    distance = [-1] * (n+1)
    for i in range(2,n+1):
        touch[i] = 1
        distance[i] = w[1][i]

    for _ in range(n-1):
        minvalue = inf
        for i in range(2,n+1):
            if 0<=distance[i]<minvalue:
                minvalue = distance[i]
                vnear = i
        edge = (touch[vnear], vnear, w[touch[vnear]][vnear])
        F.append(edge)
        for i in range(2,n+1):
            if distance[i] > distance[vnear] + w[vnear][i]:
                distance[i] = distance[vnear] + w[vnear][i]
                touch[i] = vnear
        distance[vnear] = -1

    return F


print(dijkstra(w))