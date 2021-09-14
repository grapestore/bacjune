import sys
import heapq

sys.stdin = open("inputs.text")


n,m = map(int,sys.stdin.readline().split())


arr = list(map(int,sys.stdin.readline().split()))

heapq.heapify(arr)

for _ in range(m):
  a = heapq.heappop(arr)
  b = heapq.heappop(arr)
  c = a + b
  heapq.heappush(arr,c)
  heapq.heappush(arr,c)

answer = sum(arr)
print(answer)