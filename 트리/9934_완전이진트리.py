import sys
from collections import defaultdict
sys.stdin = open('inputs.text')

k = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
mid = len(arr)//2
trees = defaultdict(list)
def tree(left,right,height):

  if height == k:
    trees[height].append(arr[left])
    return
  mid = (left+right)//2
  trees[height].append(arr[mid])
  tree(left,mid-1,height+1)
  tree(mid+1,right,height+1)

tree(0,len(arr)-1,1)
for i in range(1,k+1):
  print(*trees[i])