def solution(n):
    arr = ['4','1','2']
    answer = ''
    div = n
    while div > 0:
        mod = div%3
        if mod:
            div //= 3
        else:
            div = div//3 - 1
        answer += arr[mod]
            
    return answer[::-1]