import sys
import re
sys.stdin = open('inputs.text')

target = int(sys.stdin.readline())
que = sys.stdin.readline().rstrip()
result = map(int,re.findall(r'\d+', que))
print(sum(result))