import sys
from collections import deque
sys.stdin = open('inputs.text')


n = int(sys.stdin.readline())
dp = [[-1 for _ in range(1001)] for _ in range(1001)]
dp[1][0] = 0
def bfs():

  queue = deque([[1,0]])
  while queue:
    screen, clip = queue.popleft()
    if screen+clip == n:
      print(dp[screen][clip]+1)
      return
    if screen == 0 or screen+clip>1000:
      continue
    # copy
    if dp[screen][screen]==-1 or dp[screen][screen] > dp[screen][clip]+1:
      dp[screen][screen] = dp[screen][clip]+1
      queue.append([screen,screen])
    # paste
    if dp[screen+clip][clip]==-1 or dp[screen+clip][clip] > dp[screen][clip]+1:
      dp[screen+clip][clip] = dp[screen][clip]+1
      queue.append([screen+clip,clip])
    # minus
    if dp[screen-1][clip]==-1 or dp[screen-1][clip] > dp[screen][clip]+1:
      dp[screen-1][clip] = dp[screen][clip]+1
      queue.append([screen-1,clip])


bfs()

# n = int(input())
# q = deque()
# q.append((1, 0))
# visited = dict()
# visited[(1, 0)] = 0

# while q:
#   s,c = q.popleft()
#   if s == n:
#     print(visited[(s,c)])
#     break
#   if (s,s) not in visited.keys():
#     visited[(s,s)] = visited[(s,c)]+1
#     q.append((s,s))
#   if (s-1, c) not in visited.keys():
#     visited[(s-1, c)] = visited[(s, c)] + 1
#     q.append((s-1, c))
#   if (s+c, c) not in visited.keys():
#     visited[(s+c, c)] = visited[(s, c)] + 1
#     q.append((s+c, c))




