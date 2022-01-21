import heapq

def solution(jobs):
    heap = []
    start = -1
    end = 0
    i=0
    answer = 0
    while i<len(jobs):
        for j in jobs:
            if start<j[0]<=end:
                heapq.heappush(heap, [j[1],j[0]])
        if len(heap)>0:
            lenn,sta = heapq.heappop(heap)
            start = end
            end = start+lenn
            answer = answer + (end-sta)
            i+=1
        else:
            end+=1
    
        
    return answer//len(jobs)