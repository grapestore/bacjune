import sys

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
history = []
arr = [0]*n
last_idx = n-1
for command in cmd:
  temp = 0
  if len(command)>1:
    co, var = command.split()
    var = int(var)
  else:
    co = command

  if(co == 'D'):
    for check in history:
      if k<check<k+var:
        temp += 1
    k = k + var + temp
    continue
  elif(co == 'U'):
    for check in history:
      if k-var<=check<k:
          temp += 1
    k = k - var - temp
    continue
  elif(co == 'C'):
    arr[k] = 1
    history.append(k)
    if k == last_idx:
      k -= 1
      while(arr[k] != 0):
        k-=1
      last_idx = k
    else:
      k+=1
      while(arr[k] != 0):
        k+=1
    continue
  elif(co == 'Z'):
    comeback = history.pop()
    arr[comeback] = 0
    if comeback > last_idx:
      last_idz = comeback
    continue

answer = ''
for resolve in arr:
  if resolve == 0:
    answer += 'O'
  else:
    answer += 'X'
print(answer)