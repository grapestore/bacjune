import sys
sys.stdin = open('./inputs.text')
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = 0
for data in combinations(arr,3):
  temp = sum(data)
  if result<temp<=m:
    result = temp
print(result)
