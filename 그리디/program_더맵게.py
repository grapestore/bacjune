import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        if scoville[0]>=K:
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        new = a + b*2
        heapq.heappush(scoville,new)
        answer+=1
    if scoville[0] < K:
        return -1
    
    return answer