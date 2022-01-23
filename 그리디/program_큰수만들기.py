def solution(number, k):
    stack = []
    cnt = 0
    for x in number:
        temp = int(x)
        while stack and stack[-1]<temp and cnt<k:
            stack.pop()
            cnt+=1
        stack.append(temp)
    ## 나머지 처리
    if cnt<k:
        stack = stack[:(cnt-k)]
    answer = ''.join(map(str,stack))
    return answer