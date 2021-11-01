import sys
from collections import defaultdict

memo = defaultdict(set)
scores = defaultdict(int)
logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

for st in logs:
  number, que, score = st.split()
  memo[number].add(int(que))
  if int(score) >= scores[number+" "+que]:
    scores[number+" "+que] = int(score)
answer = []

print(scores)

