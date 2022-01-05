def check(x):
    stack = []
    for i in range(len(x)):
        if x[i] == ')':
            if len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(x[i])
            
    return True
    
def divide(w):
    openP = 0
    closeP = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return w[:i + 1], w[i + 1:]
    

def solution(p):
    answer = ''

    if not p :
        return ''
    u,v = divide(p)
    print(u)
    print(v)
    if check(u):
        return u+solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for x in u[1:len(u)-1]:
            if x == '(':
                answer += ')'
            else:
                answer += '('
            
    return answer