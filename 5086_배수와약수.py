import sys
sys.stdin = open("inputs.text")

while True:
  value1, value2 = map(int,sys.stdin.readline().split())
  if value1==0 and value2==0:
    break

  if value1>value2:
    result = value1%value2
    if result == 0:
      print('multiple')
    else:
      print('neither')
  else:
    result = value2%value1
    if result == 0:
      print('factor')
    else:
      print('neither')