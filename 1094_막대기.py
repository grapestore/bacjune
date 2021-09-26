import sys
sys.stdin = open('inputs.text')

# 비트 1의 개수 파악 #
target = int(sys.stdin.readline())
print(list(bin(target)[2:]).count('1'))



# 정석 #
target = int(sys.stdin.readline())
stack = [64]
while sum(stack) != target:
  if sum(stack)>target:
    cut = stack.pop()
    stack.append(cut//2)
  elif sum(stack)<target:
    stack.append(stack[-1]//2)


print(len(stack))