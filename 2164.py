from collections import deque
import sys


num = deque()
n = int(sys.stdin.readline())
for i in range(n):
    num.append(i+1)
while len(num) > 1:
    num.popleft()
    num.append(num.popleft())
print(num[0])



