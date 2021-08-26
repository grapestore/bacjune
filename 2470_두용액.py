import sys

num = int(input())
arr = []
result = [0,0]
min_max = 2000000000
for x in map(int,sys.stdin.readline().split()):
    arr.append(x)
arr.sort()
left = 0
right = len(arr)-1
target = 0
while right - left >0:
    if abs(arr[right] + arr[left]) == target:
        result[0] = arr[left]
        result[1] = arr[right]
        break
    if abs(arr[left] + arr[right]) < min_max:
        min_max = abs(arr[left] + arr[right])
        result[0] = arr[left]
        result[1] = arr[right]
    if arr[left] + arr[right]>0:
        right -= 1
    elif arr[left] + arr[right]<0:
        left += 1
print(result[0], result[1])