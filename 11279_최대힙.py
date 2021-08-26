import sys
import heapq

heap = []
max_heap = []
heapq.heapify(heap)
heapq.heapify(max_heap)
num = int(sys.stdin.readline())
for i in range(num):
    command = int(sys.stdin.readline())
    if command > 0:
        heapq.heappush(heap, (-command, command))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)