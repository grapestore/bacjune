import sys

sys.stdin = open('inputs.text')

que = sys.stdin.readline()
if que[0] == '0':
  if que[1] ==  'x':
    print(int(que,16))
  else:
    print(int(que,8))
else:
  print(int(que))