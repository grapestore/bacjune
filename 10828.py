import sys

stk = []
num = int(input())
for i in range(num):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stk.append(command[1])
    if command[0] == 'top':
        if len(stk)>0:
            print(stk[len(stk)-1])
        else:
            print(-1)
    if command[0] == 'size':
        print(len(stk))
    if command[0] == 'empty':
        if len(stk) > 0:
            print(0)
        else:
            print(1)
    if command[0] == 'pop':
        if len(stk)>0:
            print(stk.pop())
        else:
            print(-1)