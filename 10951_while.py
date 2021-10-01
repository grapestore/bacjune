import sys
sys.stdin = open('inputs.text')

while(True):
  a,b = map(int,sys.stdin.readline().split())
  if(a==None):
    break
  print(a+b)