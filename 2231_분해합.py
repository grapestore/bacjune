import sys
sys.stdin = open('inputs.text')

n = sys.stdin.readline().strip()
num = int(n)
min_value = num - (len(n)*9)
if min_value<0:
  min_value=0

for i in range(min_value, num):
  temp = sum(map(int, str(i)))
  result = i + temp
  if result == num:
    print(i)
    break
else:
  print(0)