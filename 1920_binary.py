import sys

def binary(start, end, target):
    global ans
    if abs(end - start) < 1:
        return
    
    mid = (start+end)//2
    #print(start,mid, end,target)
    #print(arr, arr[mid], target)
    if arr[mid] == target:
        ans = 1
        #print('target done')
        return
        
    if target < arr[mid]:
        binary(0, mid,target)
    if target > arr[mid]:
        binary(mid+1, end,target)


num1 = int(sys.stdin.readline())
arr=[]
for repeat1 in map(int,sys.stdin.readline().split()):
    arr.append(repeat1)
set(arr)
arr.sort()
num2 = int(sys.stdin.readline())
for target in map(int,sys.stdin.readline().split()):
    ans = 0
    binary(0, len(arr), target)
    print(ans)