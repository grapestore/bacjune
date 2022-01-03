
def solution(s):
    
    stack = []
    for i in s:
        if len(stack)>0 and i == stack[-1]:
            stack.pop()
            continue
        stack.append(i)
    if stack:
        return 0
    else:
        return 1