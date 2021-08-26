import sys


num, K = map(int,sys.stdin.readline().split())
arr = input()
question = []
k = K
for x in arr:
    question.append(int(x))
    
stack = []
for i in question:
    while k>0 and len(stack)>0 and stack[-1]<i:
        stack.pop()
        k -= 1
    stack.append(i)
print(''.join(map(str,stack[:num-K])))