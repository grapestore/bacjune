import sys
sys.stdin = open('inputs.text')
from itertools import combinations


def gen_combinations(arr, n):
  result =[]
  if n == 0:
    return [[]]
  for i,elem in enumerate(arr):
    for C in gen_combinations(arr[i + 1:], n-1):
      result += [[elem]+C]
  return result

while True:
  arr = list(map(int,sys.stdin.readline().split()))
  status = arr.pop(0)
  if status == 0:
    break
  for data in gen_combinations(arr,6):
    print(*data)
  print()


