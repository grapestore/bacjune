import sys
from collections import defaultdict
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
sort_ans = sorted(ans.items(), key = lambda item: item[0])
for x in sort_ans:
    if x[1] != None:
        print(x[1])
