import sys
sys.stdin = open('inputs.text')
from itertools import permutations

n = int(sys.stdin.readline())
arr = []
for i in range(1,n+1):
  arr.append(i)
for data in permutations(arr, n):
  print(*data)