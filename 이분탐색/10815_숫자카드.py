import sys
sys.stdin = open('inputs.text')
from collections import defaultdict

find = defaultdict(int)
n = int(sys.stdin.readline())
search = list(map(int,sys.stdin.readline().split()))
for data in search:
  find[data] = 0
m = int(sys.stdin.readline())
question = list(map(int,sys.stdin.readline().split()))
result = []
for confirm in question:
  if confirm in find:
    result.append(1)
  else:
    result.append(0)

print(*result)