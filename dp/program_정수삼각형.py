from collections import deque

def game(triangle,dp):
    n = len(dp)
    queue = deque([[0,0]])
    dx = [0,1]
    dp[0][0] = triangle[0][0]
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + 1
            if  0<=ny<n and dp[ny][nx] < triangle[ny][nx] + dp[y][x]:
                dp[ny][nx] = triangle[ny][nx] + dp[y][x]
                queue.append([nx,ny])
    
    return max(dp[-1])

def solution(triangle):
    answer = 0
    cost = [[0]*len(x) for x in triangle]
    answer = game(triangle, cost)
    return answer




if __name__ == "__main__":

  solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

