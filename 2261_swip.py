import sys, heapq, math
from collections import deque

def dis_check(start,end):
    if end-start < 1:
        return sys.maxsize
    mid = (start+end)//2
    data_mid = math.sqrt((heap[mid+1][1] - heap[mid][1])**2 + (heap[mid+1][0] - heap[mid][0])**2)
    return min(dis_check(start,mid), data_mid, dis_check(mid+1,end))


num = int(sys.stdin.readline())
spot = []
for x in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    spot.append(temp)
heap = deque()
spot.sort(key=lambda x: (x[0]))
distance = math.sqrt((spot[1][0] - spot[0][0])**2 + (spot[1][1] - spot[0][1])**2)
new_distance = sys.maxsize
min_data = (spot[1][0] - spot[0][0])**2 + (spot[1][1] - spot[0][1])**2
width_x = [0,0]
width_y = [0,0]
for x in range(len(spot)):
    width_x[1] = spot[x][0]
    width_x[0] = width_x[1] - distance
    width_y[1] = spot[x][1] + distance
    width_y[0] = spot[x][1] - distance
    heap.append(spot[x])
    while len(heap)>0 and (heap[0][0] < width_x[0]):
        heap.popleft()
    if len(heap)>1:
        new_distance = dis_check(0,len(heap)-1)
        if distance > new_distance:
            distance = new_distance
print(distance**2)


