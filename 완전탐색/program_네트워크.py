def dfs(start,visit,n,way):
    
    visit[start] = way
    answer = [x for x in visit]
    for next in range(n):
        if matrix[start][next]==1 and start!=next and visit[next]==-1:
            dfs(next,visit,n,way)


def solution(n, computers):
    global matrix
    matrix = computers
    answer = 0
    visit = [-1]*n
    for i in range(n):
        if visit[i] == -1:
            dfs(i,visit,n,i)
        
    return len(set(visit))