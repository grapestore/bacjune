import sys
sys.stdin = open('inputs.text')
from collections import deque


n,m = map(int,sys.stdin.readline().split())
check = [[]for _ in range(n+1)]
small = set()

for _ in range(m):
    k = int(sys.stdin.readline())
    small.add(k)

def bfs(start):
    global n
    queue = deque([start])
    dx =[1,0,-1]
    while queue:
        distance, stone, count = queue.popleft()
        for i in range(3):
            x = distance + dx[i]
            if x > 0:
                next_stone = stone + x
                if next_stone == n:
                    return count+1
                if next_stone<n and next_stone not in small and x not in check[next_stone]:
                    check[next_stone].append(x)
                    queue.append([x,next_stone,count+1])
    return -1

print(bfs([0,1,0]))
