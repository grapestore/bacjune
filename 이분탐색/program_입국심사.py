def solution(n, times):
    
    left = 1
    right = max(times)*n
    answer = right * n
    while left<=right:
        result = [0] * len(times)
        mid = (left+right)//2
        for i in range(len(times)):
            result[i] = mid//times[i]

        result_human = sum(result)
        if result_human<n:
            left = mid+1
        else:
            if mid<=answer:
                answer = mid
            right = mid-1
        
    return answer