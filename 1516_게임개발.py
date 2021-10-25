import sys
from collections import deque
sys.stdin = open('inputs.text')

score = [0]
num = int(sys.stdin.readline())
check = [[] for _ in range(num+1) ]
matrix = [[] for _ in range(num+1) ]
for i in range(1,num+1):
  temp = list(map(int,sys.stdin.readline().split()))
  length = len(temp)
  score.append(*temp[0:1])
  if temp[1] != -1:
    for j in temp[1:length]:
      if j == -1:
        break
      else:
        matrix[j].append(i)
        check[i].append(j)
count = [-1]
visited = [True] * (num+1)
queue = deque()
i = 1
for k in check[1:]:
  if len(k) == 0:
    queue.append(i)
    visited[i] = False
  count.append(len(k))
  i+=1
#result = [answer for answer in score]
result = [0] * (num+1)
temp_result = 0

print(result)

def max_find(index):
  maxvalue = 0
  for target in check[index]:
    if maxvalue<result[target]:
      maxvalue = result[target]
  return maxvalue

while queue:
  number = queue.popleft()
  temp_result+=score[number]
  for minus in matrix[number]:
    count[minus] -= 1
  for find in range(1,num+1):
    if visited[find] == True and count[find] == 0:
      visited[find] = False
      queue.append(find)
  result[number] = max_find(number) + score[number]

for answer in result[1:]:
  print(answer)

