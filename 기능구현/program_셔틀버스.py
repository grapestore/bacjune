from collections import deque

def solution(n, t, m, timetable):
    arr = deque([])
    for time in timetable:
        hour = int(time[:2])*60
        minute = int(time[3:])
        arr.append(hour+minute)
    arr = sorted(arr)
    busTime = [9*60 + t*i for i in range(n)]

    answer = 0
    idx = 0
    for bus in busTime:
        cnt = 0
        while cnt < m and idx < len(arr) and arr[idx] <= bus:
            idx+=1
            cnt+=1
        if cnt < m:
            answer = bus
        else:
            answer = arr[idx - 1] - 1
    
    return str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)