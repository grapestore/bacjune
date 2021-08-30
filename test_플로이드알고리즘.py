inf = 999
W = [
    [0,1,inf,1,5],
    [9,0,3,2,inf],
    [inf,inf,0,4,inf],
    [inf,inf,2,0,3],
    [3,inf,inf,inf,0]]




def floyd(w):
    D = w
    n = len(w)
    P = [[-1]*n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k]+D[k][j]:
                    D[i][j] = D[i][k]+D[k][j]
                    P[i][j] = k

    return D, P

D,P = floyd(W)
for x in P:
    print(x)