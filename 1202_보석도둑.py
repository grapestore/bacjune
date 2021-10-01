import sys
import heapq
sys.stdin = open('inputs.text')

n,k = map(int,sys.stdin.readline().split())

item = []
bag = []
result = 0
for _ in range(n):
    weight, value = map(int,sys.stdin.readline().split())
    heapq.heappush(item, [weight,value])
for _ in range(k):
    bag.append(int(sys.stdin.readline()))
bag.sort()

candidate = []
for bagweight in bag:
    while item and bagweight >= item[0][0]:
        w,v = heapq.heappop(item)
        heapq.heappush(candidate, -v)

    if candidate:
        result -= heapq.heappop(candidate)


print(result)

