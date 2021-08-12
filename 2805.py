import sys

def binary(start,end,target):
    global namu
    
    while(end>=start):
        mid = (start+end)//2
        answer = 0
        for x in namu_arr:
            if x>mid:
                answer += (x-mid)
        if answer >= target:
            start = mid + 19
            
        else:
            end = mid -1
    print(end)



namu,target = map(int,sys.stdin.readline().split())
namu_arr = list(map(int,sys.stdin.readline().split()))
ax(namu_arr)
binary(1,start_h,target)