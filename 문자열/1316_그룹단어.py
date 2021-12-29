import sys
sys.stdin = open('inputs.text')

num = int(sys.stdin.readline())

cnt = 0
for _ in range(num):
  arr = list(map(str,sys.stdin.readline().rstrip()))

  check = []
  
  for x in arr:
    if len(check)>0 and check[-1] != x and x in check:
      break
    check.append(x)
  else:
    cnt+=1

print(cnt)