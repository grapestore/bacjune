import sys
from collections import deque
sys.stdin = open('inputs.text')


m,n = map(int,sys.stdin.readline().split())
puddles = [[2,2]]
matrix = [[0] * (m+1) for _ in range(n+1)]

for x,y in puddles:
  matrix[y][x] = -1


for i in range(1,n+1):
  for j in range(1,m+1):
    if matrix[i][j] != -1:
      a = matrix[i-1][j]
      b = matrix[i][j-1]
      if a == -1:
        a=0
      if b == -1:
        b=0  
      matrix[i][j] = a + b
      matrix[1][1] = 1


print(matrix[-1][-1])