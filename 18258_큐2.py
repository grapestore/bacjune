from collections import deque
import sys

stk = deque()
num = int(sys.stdin.readline())
for i in range(num):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stk.append(int(command[1]))
    if command[0] == 'front':
        if len(stk) > 0:
            if isinstance(stk[0],int) == True:
                print(stk[0])
            else:
                print(-1)
        else:
            print(-1)
    if command[0] == 'back':
        if len(stk) > 0:
            if isinstance(stk[-1],int) == True:
                print(stk[-1])
            else:
                print(-1)
        else:
            print(-1)
    if command[0] == 'empty':
        if len(stk) < 1:
            print(1)
        else:
            print(0)
    if command[0] == 'size':
        print(len(stk))
    if command[0] == 'pop':
        if len(stk) > 0:
            print(stk.popleft())
        else:
            print(-1)