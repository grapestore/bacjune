import sys
from collections import defaultdict
sys.stdin = open('inputs.text')
sys.setrecursionlimit(100000)

num = int(sys.stdin.readline())
arr = defaultdict(list)
ans = {
    1:None
}
for q in range(num-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start):
    for link in arr[start]:
        if link not in ans:
            ans[link] = start
            dfs(link)

dfs(1)
for i in range(2,num+1):
  print(ans[i])