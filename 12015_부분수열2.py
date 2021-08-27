import sys
from bisect import bisect_left
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
memo = []
for data in arr:
    k = bisect_left(memo,data)
    if len(memo) <= k:
        memo.append(data)
    else:
        memo[k] = data
print(len(memo))