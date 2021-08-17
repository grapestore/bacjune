import sys

num = int(sys.stdin.readline())
arr = []
for x in range(num):
    tp = list(map(int,sys.stdin.readline().split()))
    arr.append(tp)
circle = []
stack = []
result = 0
for x in arr:
    circle.append(['L',x[0]-x[1]])
    circle.append(['R',x[0]+x[1]])
circle = sorted(circle, key=lambda x : (-x[1], x[0]))
for i in reversed(circle):
    if i[0] == 'R':
        temp = 0
        while stack:
            top = stack.pop()
            if top[0] == 'L':
                if temp == 0:
                    stack.append(['C',i[1]-top[1]])
                    break
                else:
                    stack.append(['C',i[1]-top[1]])
                    if i[1] - top[1] == temp:
                        result += 1
                        break
                    else:
                        break
            elif top[0] == 'C':
                temp = top[1] + temp
    else:
        stack.append(i)
print(result+num+1)