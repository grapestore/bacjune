import sys


stk = []
num = int(sys.stdin.readline())
for i in range(num):
    store = int(sys.stdin.readline())
    if store != 0:
        stk.append(store)
    else:
        stk.pop()
print(sum(stk))

