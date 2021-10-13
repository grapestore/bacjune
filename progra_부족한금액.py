price = 3
money = 20
count = 4



dp = [0]*2501
for i in range(1,count+1):
  dp[i] = dp[i-1] + price
if money - sum(dp) >= 0:
  print(0)
else:
  print(sum(dp)-money)
