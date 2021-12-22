import sys
sys.stdin = open('inputs.text')

k, n = map(int,sys.stdin.readline().split())
arr = []
count = []

for _ in range(k):
  arr.append(int(sys.stdin.readline().rstrip()))
  count.append(0)

right = max(arr)
left = 1
maximum = 0

while left<=right:
  mid = (right+left)//2
  for idx in range(k):
    count[idx] = arr[idx]//mid
  check = sum(count)
  if check>=n:
    maximum = mid
    left = mid+1
  elif check<n:
    right = mid-1

print(maximum)
  
