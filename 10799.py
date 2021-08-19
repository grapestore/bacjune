import sys



arr = []
question = sys.stdin.readline().strip()
for i in question:
    arr.append(i)
stack = []
result = []
for que in arr:
    if que == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(' and temp == 0:
                stack.append(1)
                break
            elif top == '(' and temp > 0:
                result.append(temp+1)
                stack.append(temp)
                break
            else:
                temp += top
    else:
        stack.append(que)

print(sum(result))