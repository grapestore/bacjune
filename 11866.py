from collections import deque
import sys

n,start = map(int,sys.stdin.readline().split())
num = []
for i in range(n):
    num.append(i+1)
gap = start - 1
result = []
start = start - 1
result.append(num.pop(start))
start += gap
while len(result) != n:
    while start >= len(num):
        start = start - len(num)
    result.append(num.pop(start))
    
    start += gap
print('<'+', '.join(map(str,result))+'>')