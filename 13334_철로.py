import sys
import heapq


num = int(sys.stdin.readline())
arr = []
for i in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    if temp[0] > temp[1]:
        arr.append([temp[1],temp[0]])
    else:
        arr.append([temp[0],temp[1]])
dis = [0]
distance = int(sys.stdin.readline())
dis.append(distance)
queue = []
arr.sort(key = lambda x: (x[1],x[0]))
i = 0
max = 0
for line in arr:
    dis[1] = line[1]
    dis[0] = dis[1] - distance
    heapq.heappush(queue, line)
    while queue and queue[0][0] < dis[0]:
        heapq.heappop(queue)
    if len(queue) > max:
        max = len(queue)
print(max)

