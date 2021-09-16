import sys
sys.stdin = open("inputs.text")

num = int(sys.stdin.readline())
count = 0

for _ in range(num):
  question = list(sys.stdin.readline().rstrip())
  stack = []
  stable = True
  for i in question:
    if len(stack)>0 and (stack[-1] != i and i in stack):
      stable = False
      continue
    stack.append(i)
  if stable == True:
    count += 1

print(count)