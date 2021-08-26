import sys

question = list(input())

stack = []
stable = False
for i in question:
    if stable == False:
        if i == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(' and t == 0:
                    stack.append(2)
                    break
                elif top == '(' and t > 0:
                    stack.append(t * 2)
                    break
                elif top == '[':
                    stable = True
                    print(0)
                    break
                elif top > 0:
                    if t == 0:
                        t = top
                    else:
                        t = t + top
        elif i == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top == '[' and t == 0:
                    stack.append(3)
                    break
                elif top == '[' and t > 0:
                    stack.append(t * 3)
                    break
                elif top == '(':
                    stable = True
                    print(0)
                    break
                elif top > 0:
                    if t == 0:
                        t = top
                    else:
                        t = t + top
                

        else:
            stack.append(i)
if stable == False:
    try:
        print(sum(stack))
    except:
        print(0)