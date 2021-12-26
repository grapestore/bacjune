import sys
from collections import deque
sys.stdin = open('inputs.text')

max_number = 10000
prime = [False] * max_number
prime[0] = True
prime[1] = True


def find_prime():
  for i in range(2,max_number//2+1):
    if prime[i] == False:
      for index in range(i*i,max_number,i):
        if index <= max_number:
          prime[index] = True

find_prime()

def bfs(cur, target):
  visit = [False] * max_number
  queue = deque([[cur,0]])
  while queue:
    cur_prime, depth = queue.popleft()
    visit[cur_prime] = True
    if cur_prime==target:
      print(depth)
      return
    cur = str(cur_prime)
    one = int(cur[3])
    ten = int(cur[2])
    hund = int(cur[1])
    thousand = int(cur[0])

    test1 = cur_prime - one
    test2 = cur_prime - ten * 10
    test3 = cur_prime - hund * 100
    test4 = cur_prime - thousand * 1000

    for x in range(10):
      a = test1 + x
      b = test2 + x * 10
      c = test3 + x * 100
      d = test4 + x * 1000
      if 1000<=a<=9999 and prime[a]==False and visit[a]== False:
        visit[a] = True
        queue.append([a, depth+1])
      if 1000<=b<=9999 and prime[b]==False and visit[b]== False:
        visit[b] = True
        queue.append([b, depth+1])
      if 1000<=c<=9999 and prime[c]==False and visit[c]== False:
        visit[c] = True
        queue.append([c, depth+1])
      if 1000<=d<=9999 and prime[d]==False and visit[d]== False:
        visit[d] = True
        queue.append([d, depth+1])
  print('Impossible')
  return

n = int(sys.stdin.readline())
for _ in range(n):
  curr, target = map(int,sys.stdin.readline().split())
  bfs(curr, target)
