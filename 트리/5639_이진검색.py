import sys
sys.stdin = open('inputs.text')
sys.setrecursionlimit(10**6)

arr = []
while True:
  try:
    arr.append(int(sys.stdin.readline()))
  except:
    break

def insert(start,end):
  if start > end:
    return

  for i in range(start+1,end+1):
    if arr[i] > arr[start]:
      div = i
      break
  
  insert(start+1,div-1)
  insert(div,end)
  print(arr[start])
    

insert(0,len(arr)-1)
