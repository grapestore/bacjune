import sys, heapq, math

num = int(sys.stdin.readline())
spot = []
for x in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    spot.append(temp)
heap = []
spot.sort(key=lambda x: (x[0]))
distance = math.sqrt((spot[1][0] - spot[0][0])**2 + (spot[1][1] - spot[0][1])**2)
new_distance = sys.maxsize
min_data = (spot[1][0] - spot[0][0])**2 + (spot[1][1] - spot[0][1])**2
width_x = [0,0]
width_y = [0,0]
for spot_lo in spot:
    width_x[1] = spot_lo[0]
    width_x[0] = width_x[1] - distance
    width_y[1] = spot_lo[1] + distance
    width_y[0] = spot_lo[1] - distance
    heapq.heappush(heap, spot_lo)
    while len(heap)>0 and (heap[0][0] < width_x[0]):
        heapq.heappop(heap)
    if len(heap)>1:
        for i in range(0,len(heap)-1):
            for j in range(i+1,len(heap)):
                new_distance = math.sqrt((heap[i][0] - heap[j][0])**2 + (heap[i][1] - heap[j][1])**2)
                if distance > new_distance:
                    min_data = (heap[i][0] - heap[j][0])**2 + (heap[i][1] - heap[j][1])**2
                    distance = new_distance
                    break
print(min_data)


