import sys
import re
sys.stdin = open('inputs.text')

que = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()

check = re.findall('[a-zA-Z]', que)
check = "".join(check)

if find in check:
  print(1)
else:
  print(0)