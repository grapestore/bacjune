import sys

num = int(sys.stdin.readline())
stk = []
for i in range(num):
    stk.append(int(input()))
count = 1
right_height = stk.pop()
while len(stk)>0:
    right_current = stk.pop()
    if right_current > right_height:
        right_height = right_current
        count += 1
print(count)

