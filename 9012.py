import sys


num = int(sys.stdin.readline())
for i in range(num):
    stable = False
    stk = []
    result = []
    last = []
    stk = input()
    for j in range(len(stk)):
        result.append(stk[j])
    for k in result:
        if k == '(':
            last.append(1)
        if k == ')':
            if len(last):
                last.pop()
            else:
                stable = True
                print('No')
                break

    if stable == False:
        if len(last)>0:
            print('NO')
        else:
            print('YES')
