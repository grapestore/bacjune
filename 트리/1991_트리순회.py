import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
tree = dict()
root = 'A'
for _ in range(n):
  parent, left, right = sys.stdin.readline().split()
  tree[parent] = [left,right]

def front(start):
  answer = start
  if tree[start][0] != '.':
    answer += front(tree[start][0])
  if tree[start][1] != '.':
    answer += front(tree[start][1])
  return answer

def middle(start):
  answer = ''
  if tree[start][0] != '.':
    answer += middle(tree[start][0])
  answer += start
  if tree[start][1] != '.':
    answer += middle(tree[start][1])
  return answer

def end(start):
  answer = ''
  if tree[start][0] != '.':
    answer += end(tree[start][0])
  if tree[start][1] != '.':
    answer += end(tree[start][1])
  answer += start
  return answer

print(front(root))
print(middle(root))
print(end(root))