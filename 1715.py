import heapq
import sys

num = int(sys.stdin.readline())
heap = []
result = []
stable = False
for i in range(num):
    heapq.heappush(heap, int(sys.stdin.readline()))
heapq.heapify(heap)
if len(heap) < 2:
    stable = True
    print(0)
if stable == False:
    while len(heap)>1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        temp_result = temp1 + temp2
        result.append(temp_result)
        heapq.heappush(heap, temp_result)



    print(sum(result))

