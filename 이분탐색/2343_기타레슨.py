import sys
sys.stdin = open('inputs.text')

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

left = max(arr)
right = sum(arr)


def cd_cnt():
  cnt = 0
  temp = 0
  for i in range(n):
    if temp + arr[i] > mid:
      cnt+=1
      temp=0
    temp = temp + arr[i]
  else:
    if temp:
      cnt += 1
  return cnt

while left<=right:
  mid = (left+right)//2
  cnt = cd_cnt()
  if cnt>m:
    left = mid + 1
  elif cnt<=m:
    right = mid - 1

print(left)
