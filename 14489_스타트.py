import sys
sys.stdin = open('inputs.text')

arr = [1,1,1,2,2,3,4,5,7,9]

n = int(sys.stdin.readline())
for _ in range(n):
  num = int(sys.stdin.readline())
  if num > len(arr):
    for i in range(len(arr),num+1):
      arr.append(arr[i-1]+arr[i-5])
    print(arr[num-1])
  else:
    print(arr[num-1])
