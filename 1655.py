import sys
import heapq

heap_left = []
heap_right = []

num = int(sys.stdin.readline())
for x in range(num):
    value = int(sys.stdin.readline())
    if x % 2==0:
        heapq.heappush(heap_left, -value)
    else:
        heapq.heappush(heap_right, value)
    if len(heap_left)>0 and len(heap_right)>0:
        if -heap_left[0]>heap_right[0]:
            temp1 = heapq.heappop(heap_left)
            temp2 = heapq.heappop(heap_right)
            heapq.heappush(heap_left, -temp2)
            heapq.heappush(heap_right, -temp1)

    print(-heap_left[0])
    