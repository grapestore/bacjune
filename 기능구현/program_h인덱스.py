def solution(citations):
    
    if len(citations)==1 and citations[0]>=1:
        return 1
    
    answer = 0
    for i in range(0,1001):
        cnt = 0
        for x in citations:
            if x>=i:
                cnt+=1
        if cnt>=i:
            answer=i
    return answer