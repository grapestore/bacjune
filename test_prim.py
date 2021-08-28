inf = 999
w = [
    [-1,-1,-1,-1,-1,-1],
    [-1,0,1,3,inf,inf],
    [-1,1,0,3,6,inf],
    [-1,3,3,0,4,2],
    [-1,inf,6,4,0,5],
    [-1,inf,inf,2,5,0]
]

def prim(w):
    n = len(w)-1
    F = []
    nearest = [-1] * (n+1)
    distance = [-1] * (n+1)
    for i in range(2,n+1):
        nearest[i] = 1
        distance[i] = w[1][i]

    for _ in range(n-1):
        minvalue = inf
        for i in range(2,n+1):
            if 0<=distance[i]<minvalue:
                minvalue = distance[i]
                vnear = i
        edge = (nearest[vnear], vnear, w[nearest[vnear]][vnear])
        F.append(edge)
        distance[vnear] = -1
        for i in range(2,n+1):
            if distance[i] > w[vnear][i]:
                distance[i] = w[vnear][i]
                nearest[i] = vnear

    return F


print(prim(w))