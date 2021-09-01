import sys
sys.stdin = open('inputs.text')

n = int(sys.stdin.readline())
arr = [0]
dp = [0] * (n+1)
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

if n==1:
    dp[1] = arr[1]
elif n==2:
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]
else:
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[-1])