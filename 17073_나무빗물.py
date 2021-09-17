import sys

sys.stdin = open('inputs.text')


num, water = map(int,sys.stdin.readline().split())

tree = [[] for _ in range(num+1)]

for _ in range(num-1):
  a,b = map(int,sys.stdin.readline().split())
  tree[a] += [b]
  tree[b] += [a]
leaf_node_count = 0;
for i in range(2,num+1):
  if len(tree[i]) == 1:
    leaf_node_count += 1
answer = round((water/leaf_node_count),10)
print(answer)