import sys
sys.stdin = open('inputs.text')


n = int(sys.stdin.readline())
que = sys.stdin.readline()
result = 0

for i in range(n):
  result += int(que[i])


print(result)