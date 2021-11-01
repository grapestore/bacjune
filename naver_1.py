import sys
from collections import defaultdict


id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k = 3
memo = defaultdict(int)
for days in id_list:
  for ids in set(days.split()):
    if memo[ids] < k:
      memo[ids] += 1

print(sum(memo.values()))