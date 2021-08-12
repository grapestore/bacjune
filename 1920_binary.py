import sys

def binary(arr,target):
    global ans
    if len(arr) < 1:
        return ans
    mid = len(arr)//2
    #print(arr, arr[mid], target)
    if arr[mid] == target:
        ans = 1
        #print('target done')
        return ans
        
    if target < arr[mid]:
        binary(arr[:mid],target)
    if target > arr[mid]:
        binary(arr[mid+1:],target)


num1 = int(sys.stdin.readline())
A=[]
for repeat1 in map(int,sys.stdin.readline().split()):
    A.append(repeat1)
A.sort()
num2 = int(sys.stdin.readline())
for target in map(int,sys.stdin.readline().split()):
    ans = 0
    binary(A,target)
    print(ans)