import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort(reverse=True)

dp = [0]*(n+1)
i=1
while arr:
  sequ = arr.pop()
  dp[i] = dp[i-1]+sequ
  i+=1
print(sum(dp))