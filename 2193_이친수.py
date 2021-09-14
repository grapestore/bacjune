import sys
sys.stdin = open("inputs.text")


n = int(sys.stdin.readline())
start = 2**(n-1)
end = 2**(n)
for x in range(start,end):
  