import sys

def binary(start,end,target):
    global namu
    if end - start < 1 :
        return
    
    mid = (start+end)//2
    answer = 0
    for x in namu_arr:
        if x>mid:
            answer += x-mid
    if answer >= target:
        result.append(mid)
        binary(mid+1,end,target)
    if answer < target:
        binary(start,mid-1,target)



namu,target = map(int,sys.stdin.readline().split())
namu_arr = list(map(int,sys.stdin.readline().split()))
result = []
start_h = max(namu_arr)
binary(0,start_h,target)
#print(result)
print(max(result))