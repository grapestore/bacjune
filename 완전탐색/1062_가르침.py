import sys
sys.stdin = open('./inputs.text')
from itertools import combinations

base = ['a','n','t','i','c']
need = []

n, k = map(int,sys.stdin.readline().split())
rest_num = k-5
if k<5:
  print(0)
  exit(0)

words = []

for x in range(n):
  inputdata = sys.stdin.readline().rstrip()
  result = inputdata[4:-4]
  words.append(result)
  for char in result:
    if char not in base and char not in need:
      need.append(char)
max_count = 0
if rest_num>len(need):
  rest_num=len(need)
for combi in combinations(need,rest_num):
  find = base+list(combi)
  count = 0
  for word in words:
    for alpha in word:
      if alpha not in find:
        break
    else:
      count+=1
  if count >= max_count:
    max_count=count


print(max_count)